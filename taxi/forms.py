from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import forms

from taxi.models import Car, Manufacturer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))
