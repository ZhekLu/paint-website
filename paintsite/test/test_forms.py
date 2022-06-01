from django.test import TestCase

from paintsite.forms import RegisterUserForm, LoginForm, ChangeUserInfoForm, PSPasswordChangeForm, SubTagForm, \
    SearchForm, PictureForm, UserCommentForm, GuestCommentForm
from paintsite.models import User


class LoginFormTest(TestCase):

    def test_username_field_label(self):
        form = LoginForm()
        self.assertTrue(
            form.fields['username'].label == 'Username'
        )

    def test_password_field_label(self):
        form = LoginForm()
        self.assertTrue(
            form.fields['password'].label == 'Password'
        )


class ChangeUserInfoFormTest(TestCase):

    def test_username_field_label(self):
        form = ChangeUserInfoForm()
        self.assertTrue(
            form.fields['username'].label == 'Username'
        )

    def test_email_field_label(self):
        form = ChangeUserInfoForm()
        self.assertTrue(
            form.fields['email'].label == 'Email address'
        )

    def test_first_name_field_label(self):
        form = ChangeUserInfoForm()
        self.assertTrue(
            form.fields['first_name'].label == 'First name'
        )

    def test_last_name_field_label(self):
        form = ChangeUserInfoForm()
        self.assertTrue(
            form.fields['last_name'].label == 'Last name'
        )


class PSPasswordChangeFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Big', last_name='Bob',
                            is_activated=True, send_messages=True, username='big_bob')

    def test_username_field_label(self):
        form = PSPasswordChangeForm(user=User.objects.get(id=1))
        self.assertTrue(
            form.fields['old_password'].label == 'Old password'
        )

    def test_email_field_label(self):
        form = PSPasswordChangeForm(user=User.objects.get(id=1))
        self.assertTrue(
            form.fields['new_password1'].label == 'New password'
        )

    def test_first_name_field_label(self):
        form = PSPasswordChangeForm(user=User.objects.get(id=1))
        self.assertTrue(
            form.fields['new_password2'].label == 'New password confirmation'
        )


class RegisterUserFormTest(TestCase):

    def test_different_passwords(self):
        form_data = {'username': 'unique', 'email': 'good@mail.ru',
                     'password': 'hArD1234_!', 'password_confirm': 'hArD1234_'}
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_same_passwords(self):
        form_data = {'username': 'unique', 'email': 'good@mail.ru',
                     'password': 'hArD1234_!', 'password_confirm': 'hArD1234_!'}
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_save(self):
        form_data = {'username': 'unique', 'email': 'good@mail.ru',
                     'password': 'hArD1234_!', 'password_confirm': 'hArD1234_!'}
        form = RegisterUserForm(data=form_data)
        self.assertEquals(0, User.objects.all().count())
        form.save()
        self.assertEquals(User.objects.all().count(), 1)


class SubTagFormTest(TestCase):

    def test_order_field_label(self):
        form = SubTagForm()
        self.assertTrue(
            form.fields['order'].label == 'Order'
        )

    def test_super_tag_field_label(self):
        form = SubTagForm()
        self.assertTrue(
            form.fields['super_tag'].label == 'Parent tag'
        )


class SearchFormTest(TestCase):

    def test_keyword_field_label(self):
        form = SearchForm()
        self.assertTrue(
            form.fields['keyword'].label == 'Search...'
        )


class PictureFormTest(TestCase):

    def test_tag_field_label(self):
        form = PictureForm()
        self.assertTrue(
            form.fields['tag'].label == 'Tag'
        )

    def test_image_field_label(self):
        form = PictureForm()
        self.assertTrue(
            form.fields['image'].label == 'Picture'
        )

    def test_author_field_label(self):
        form = PictureForm()
        self.assertTrue(
            form.fields['author'].label == 'Picture author'
        )


class UserCommentFormTest(TestCase):

    def test_content_field_label(self):
        form = UserCommentForm()
        self.assertTrue(
            form.fields['content'].label == 'Content'
        )


class GuestCommentFormTest(TestCase):

    def test_content_field_label(self):
        form = GuestCommentForm()
        self.assertTrue(
            form.fields['content'].label == 'Content'
        )

    def test_captcha_field_label(self):
        form = GuestCommentForm()
        self.assertTrue(
            form.fields['captcha'].label == 'Enter text from the image'
        )
