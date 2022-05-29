from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import User, SuperTag, SubTag, PictureBoard, Comment
from .apps import user_registered


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    password_confirm = forms.CharField(label='Password confirmation', widget=forms.PasswordInput,
                                       help_text='Confirm ur password')

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
        user_registered.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm',
                  'first_name', 'last_name', 'send_messages')


class SubTagForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(
        queryset=SuperTag.objects.all(),
        empty_label=None,
        label='Parent tag',
        required=True
    )

    class Meta:
        model = SubTag
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')


class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureBoard
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}


# Comments

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active', )
        widgets = {'author': forms.HiddenInput, 'pp': forms.HiddenInput}


class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Enter text from the image',
                           error_messages={'invalid': 'Wrong input'})

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'pp': forms.HiddenInput}
