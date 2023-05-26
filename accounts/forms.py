from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Last Name'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Email Address'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Phone Number'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

# code for giving css to form inputs

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     for fields in self.fields:
    #         self.fields[fields].widget.attrs['class'] = ''