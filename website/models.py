from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), 1, "Published")


class AddArt(models.Model):
    """add artwork to website """
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class RegularCommission(models.Model):
    """contact form for users to request regular commisions"""
    character_reference = models.CharField(max_length=100)
    character_owner = models.CharField(max_length=100)
    commission_type = models.CharField(max_length=100)
    type_option = models.CharField(max_length=100,)
    character_personality = models.CharField(max_length=100)
    pose = models.CharField(max_length=100)
    other_info = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class ReferenceSheetCommission(models.Model):
    """contact form for users to request reference sheet commisions"""
    character_reference = models.CharField(max_length=100)
    character_owner = models.CharField(max_length=100)
    design_changes = models.CharField(max_length=100)
    add_ons = models.CharField(max_length=100)
    other_info = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class CustomCommissions(models.Model):
    """contact form for users to request custom commisions"""
    theme = models.CharField(max_length=100)
    colours = models.CharField(max_length=100)
    traits = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    accessories = models.CharField(max_length=100)
    other_info = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class Comment(models.Model):
    """comment model for autharised users to comment on artwork
    on gallery page"""
    post = models.ForeignKey(AddArt, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0),
    ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.name} {self.body}"
