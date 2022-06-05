from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError

from .models import User, SuperTag, SubTag, PictureBoard, Comment
from .apps import user_registered


# User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "form-control"
            })

        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder": "Password",
                "class": "form-control"
            })


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address',
                             widget=forms.EmailInput(
                                 attrs={
                                     "placeholder": "Enter Email",
                                     "class": "form-control"
                                 }
                             ))

    def __init__(self, *args, **kwargs):
        super(ChangeUserInfoForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        )
        self.fields['first_name'].widget = forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        )
        self.fields['last_name'].widget = forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        )
        self.fields['send_messages'].widget = forms.CheckboxInput(
            attrs={
                "placeholder": "Want to be notified by email",
                "class": "form-control"
            }
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')


class PSPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PSPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "placeholder": "Previous password",
                "class": "form-control"
            }
        )
        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": "New password",
                "class": "form-control"
            })
        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": "New password confirmation",
                "class": "form-control"
            })


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address',
                             widget=forms.EmailInput(
                                 attrs={
                                     "placeholder": "Enter Email",
                                     "class": "form-control"
                                 }))
    password = forms.CharField(label='Password',
                               help_text=password_validation.password_validators_help_text_html(),
                               widget=forms.PasswordInput(
                                   attrs={
                                       "placeholder": "Password",
                                       "class": "form-control"
                                   }
                               ))
    password_confirm = forms.CharField(label='Password confirmation',
                                       help_text='Confirm your password',
                                       widget=forms.PasswordInput(
                                           attrs={
                                               "placeholder": "Password Confirmation",
                                               "class": "form-control"
                                           }
                                       ))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        )
        self.fields['first_name'].widget = forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        )
        self.fields['last_name'].widget = forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        )
        self.fields['send_messages'].widget = forms.CheckboxInput(
            attrs={
                "placeholder": "Want to be notified by email",
                "class": "form-control"
            }
        )

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password and password_confirm and password != password_confirm:
            errors = {'password_confirm': ValidationError(
                'Passwords are not same.', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registered.send(RegisterUserForm, instance=user, request=self.request)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm',
                  'first_name', 'last_name', 'send_messages')


# Pictures

class SubTagForm(forms.ModelForm):
    super_tag = forms.ModelChoiceField(
        queryset=SuperTag.objects.all(),
        empty_label=None,
        label='Parent tag',
        required=True
    )

    class Meta:
        model = SubTag
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='Search...')


class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureBoard
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}


# Comments

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'author': forms.HiddenInput, 'pp': forms.HiddenInput}


class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Enter text from the image',
                           error_messages={'invalid': 'Wrong input'})

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'pp': forms.HiddenInput}
