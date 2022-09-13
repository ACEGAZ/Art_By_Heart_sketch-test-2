from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import regular_commission
from .models import reference_sheet_commission
from .models import custom_commissions
from .models import add_art
from .models import comment


class RegularCommissionForm(ModelForm):
    class Meta:
        model = regular_commission
        fields = '__all__'


class ReferenceSheetForm(ModelForm):
    class Meta:
        model = reference_sheet_commission
        fields = '__all__'


class CustomForm(ModelForm):
    class Meta:
        model = custom_commissions
        fields = '__all__'


class UploadArt(ModelForm):
    class Meta:
        model = add_art
        fields = '__all__'


class AddCommentForm(ModelForm):
    class Meta:
        model = comment
        fields = ('post', 'name', 'body')