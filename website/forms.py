from django.forms import ModelForm
from .models import RegularCommission
from .models import ReferenceSheetCommission
from .models import CustomCommissions
from .models import AddArt


class RegularCommissionForm(ModelForm):
    """regular form for commission_view """
    class Meta:
        """creates all fields for RegularCommissionForm """
        model = RegularCommission
        fields = '__all__'


class ReferenceSheetForm(ModelForm):
    """reference sheet form for commission_view """
    class Meta:
        """creates all fields for ReferenceSheetForm """
        model = ReferenceSheetCommission
        fields = '__all__'


class CustomForm(ModelForm):
    """custom form for commission_view """
    class Meta:
        """creates all fields for CustomForm """
        model = CustomCommissions
        fields = '__all__'


class UploadArt(ModelForm):
    """upload art form for uploading art as admin """
    class Meta:
        """creates all fields for UploadArt """
        model = AddArt
        fields = '__all__'
