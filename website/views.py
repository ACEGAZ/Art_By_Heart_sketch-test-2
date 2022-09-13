import pprint
import cloudinary.uploader
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import RegularCommissionForm, ReferenceSheetForm, CustomForm, UploadArt, AddCommentForm
from .models import add_art, comment



def index(request):
    return render(request, 'index.html')


def add_comment_success(request):
    return render(request, 'add_comment_success.html')


def upload_art_view(request):
    if request.method == 'POST':
        upload_art_form = UploadArt(request.POST, request.FILES)
        if upload_art_form.is_valid():
            upload_art_form.save()
        return render(request, 'art_upload_success.html')
    upload_art_form = UploadArt()
    context = {'upload_art_form': upload_art_form}
    return render(request, 'admin_upload_art.html', context)


def display_artwork(request):
    pictures = add_art.objects.all()
    comments = comment.objects.all()
    context = {'pictures': pictures,
               'comments': comments}
    return render(request, 'gallery.html', context)


# def AddCommentView(request, _id):
#     if request.method == 'POST':
#         add_comment_form = AddCommentForm(request.POST)
#         if add_comment_form.is_valid():
#             add_comment_form = add_comment_form.save(commit=False)
#             add_comment_form.author = request.user
#             add_comment_form.save()
#         return render(request, 'add_comment_success.html')
#     add_comment_form = AddCommentForm()
#     context = {'add_comment_form': add_comment_form}
#     context["comment_id"] = comment.objects.get(_id=_id)
#     return render(request, 'add_comment.html', context)

class AddCommentView(CreateView):
    model = comment
    template_name = 'add_comment.html'
    fields = ('author', 'post', 'name', 'body')





# def UpdateCommentView(request, _id):
#     context = {}
#     obj = get_object_or_404(comment, _id=_id)
#     form = AddCommentForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/"+id)
#     update_comment_form = AddCommentForm()
#     context = {'update_comment_form': update_comment_form}
#     return render(request, "update_comment.html", context)



class UpdateCommentView(UpdateView):
    model = comment
    template_name = 'website/update_comment.html'
    fields = ('author', 'post', 'name', 'body')
    context_object_name = 'update_comment'





def commission_view(request):
    if request.method == 'POST':
        regular_form = RegularCommissionForm(request.POST)
        if regular_form.is_valid():
            regular_form.save()
            subject = request.POST.get('subject', 'New Regular Commission')
            character_reference = request.POST.get('character_reference', '')
            character_owner = request.POST.get('character_owner', '')
            commission_type = request.POST.get('commission_type', '')
            type_option = request.POST.get('type_option', '')
            character_personality = request.POST.get('character_personality', '')
            pose = request.POST.get('pose', '')
            other_info = request.POST.get('other_info', '')
            email = request.POST.get('email', '')
            message_list = {'character_reference': character_reference,
                            'character_owner': character_owner,
                            'commission_type': commission_type,
                            'type_option': type_option,
                            'character_personality': character_personality,
                            'pose': pose,
                            'other_info': other_info,
                            'email': email}
            message = pprint.pformat(message_list, sort_dicts=False)

            try:
                send_mail(subject, message, 'huemann49@gmail.com', ['huemann49@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'success.html')

    reference_form = ReferenceSheetForm(request.POST)
    if reference_form.is_valid():
        reference_form.save()
        subject = request.POST.get('subject', 'Reference Sheet Commission')
        character_reference = request.POST.get('character_reference', '')
        character_owner = request.POST.get('character_owner', '')
        design_changes = request.POST.get('design_changes', '')
        add_ons = request.POST.get('add_ons', '')
        other_info = request.POST.get('other_info', '')
        email = request.POST.get('email', '')
        message_list = {'character_reference': character_reference,
                        'character_owner': character_owner,
                        'design_changes': design_changes,
                        'add_ons': add_ons,
                        'other_info': other_info,
                        'email': email}
        message = pprint.pformat(message_list, sort_dicts=False)

        try:
            send_mail(subject, message, 'huemann49@gmail.com', ['huemann49@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'success.html')

    custom_form = CustomForm(request.POST)
    if custom_form.is_valid():
        custom_form.save()
        subject = request.POST.get('subject', 'Custom Commission')
        theme = request.POST.get('theme', '')
        colours = request.POST.get('colours', '')
        traits = request.POST.get('traits', '')
        gender = request.POST.get('gender', '')
        breed = request.POST.get('breed', '')
        accessories = request.POST.get('accessories', '')
        other_info = request.POST.get('other_info', '')
        email = request.POST.get('email', '')
        message_list = {'theme': theme,
                        'colours': colours,
                        'traits': traits,
                        'gender': gender,
                        'breed': breed,
                        'accessories': accessories,
                        'other_info': other_info,
                        'email': email}
        message = pprint.pformat(message_list, sort_dicts=False)

        try:
            send_mail(subject, message, 'huemann49@gmail.com', ['huemann49@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'success.html')

    custom_form = CustomForm()
    regular_form = RegularCommissionForm()
    reference_form = ReferenceSheetForm()
    context = {'reference_form': reference_form,
               'regular_form': regular_form,
               'custom_form': custom_form}
    return render(request, 'commissions.html', context)


