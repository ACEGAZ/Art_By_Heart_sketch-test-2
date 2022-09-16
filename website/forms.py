from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import RegularCommission
from .models import ReferenceSheetCommission
from .models import CustomCommissions
from .models import AddArt



class RegularCommissionForm(ModelForm):
    class Meta:
        model = RegularCommission
        fields = '__all__'


class ReferenceSheetForm(ModelForm):
    class Meta:
        model = ReferenceSheetCommission
        fields = '__all__'


class CustomForm(ModelForm):
    class Meta:
        model = CustomCommissions
        fields = '__all__'


class UploadArt(ModelForm):
    class Meta:
        model = AddArt
        fields = '__all__'
