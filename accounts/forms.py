from django import forms

from .models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'ایمیل'}
        )
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'پسورد'}
        )
    )


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'ایمیل'}
        )
    )
    full_name = forms.CharField(
        label="نام ",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'نام کامل'}
        )
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'پسورد'}
        )
    )


class ManagerLoginForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': ''}
        )
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': ''}
        )
    )


class EditProfileForm(forms.ModelForm):
    full_name = forms.CharField(label='نام و نام خانوادگی')
    email = forms.EmailField(label='ایمیل')
    class Meta:
        model = User
        fields = ['full_name', 'email']
