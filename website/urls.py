from django.urls import path, include
from . import views
# from .views import AddCommentView, UpdateCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    # path('', views.index, name='index'),
    # path('gallery', views.display_artwork, name='gallery'),
    # path('commissions', views.commission_view, name='commissions'),
    # path('admin_upload_art', views.upload_art_view, name='admin_upload_art'),
    # path('add_comment_success', views.add_comment_success, name='add_comment_success'),
]