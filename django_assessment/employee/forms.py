from django import forms
from . import models

# Django form for the Employees


class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['full_name', 'address', 'email', 'phone_number', 'image']

    def clean(self):
        cleaned_data = super(EmployeeCreationForm, self).clean()
        full_name = cleaned_data.get('full_name')
        phone_number = self.cleaned_data.get('phone_number')
        address = self.cleaned_data.get('address')

        if len(full_name) < 5:
            self._errors['full_name'] = self.error_class(
                ["Should contain more than 5 characters"])
        if len(address) < 5:
            self._errors['address'] = self.error_class(
                ["Should contain more than 5 characters"])
        if len(phone_number) < 9:
            self._errors['phone_number'] = self.error_class(
                ["Phone number cannot be less the 10 characters"])

        return self.cleaned_data
