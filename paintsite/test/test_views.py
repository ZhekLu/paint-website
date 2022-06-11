from django.test import TestCase
from django.urls import reverse

from paintsite.forms import UserCommentForm, GuestCommentForm
from paintsite.models import PictureBoard, User
from paintsite.test.model_factories import PictureBoardFactory, CommentFactory


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pp_num = 13
        for _ in range(pp_num):
            PictureBoardFactory.create()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/home/index.html')

    def test_pp_num_is_ten(self):
        resp = self.client.get(reverse('paintsite:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(PictureBoard.objects.all().count(), 13)
        self.assertEqual(len(resp.context['pps']), 10)


class OtherPageViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/index/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:other', args=('index',)))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:other', args=('index',)))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/home/index.html')


class ProfileViewTest(TestCase):

    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')

    def test_profile_form_success(self):
        self.response = self.client.login(username='test_name',
                                          password='1234_5678!')
        self.response = self.client.get(reverse('paintsite:profile'))
        self.assertTrue(200, self.response.status_code)
        self.assertTemplateUsed(self.response, 'paintsite/profile/profile.html')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('paintsite:profile'))
        self.assertRedirects(resp, '/accounts/login/?next=%2Faccounts%2Fprofile%2F')


class PSLoginViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:login'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/authentication/login.html')


class PSLogoutViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')

        self.client.login(username='test_name', password='1234_5678!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/logout/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:logout'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:logout'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/authentication/logout.html')


class ChangeUserInfoViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')

        self.client.login(username='test_name', password='1234_5678!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/profile/change/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:profile_change'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:profile_change'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile/profile_edit.html')


class PSPasswordChangeViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')

        self.client.login(username='test_name', password='1234_5678!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/password/change/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:password_change'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:password_change'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile/profile_password_change.html')


class RegisterUserViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/register/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:register'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:register'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/authentication/register.html')


class RegisterDoneViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/register/done/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:register_done'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:register_done'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/authentication/register_done.html')


# TODO! Register: activate user test

class DeleteUserViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')

        self.client.login(username='test_name', password='1234_5678!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/accounts/profile/delete/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:profile_delete'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:profile_delete'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile/profile_delete.html')


class ByTagViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        picture = PictureBoardFactory.create()
        resp = self.client.get(f'/{picture.tag.pk}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        picture = PictureBoardFactory.create()
        resp = self.client.get(reverse('paintsite:by_tag', kwargs={'pk': picture.tag.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        picture = PictureBoardFactory.create()
        resp = self.client.get(reverse('paintsite:by_tag', kwargs={'pk': picture.tag.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/home/by_tag.html')


class DetailViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')
        self.pp = PictureBoardFactory.create()
        CommentFactory.create(pp=self.pp)
        CommentFactory.create(pp=self.pp)
        CommentFactory.create()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(f'/{self.pp.tag.pk}/{self.pp.pk}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:detail',
                                       kwargs={'pk': self.pp.pk, 'tag_pk': self.pp.tag.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:detail',
                                       kwargs={'pk': self.pp.pk, 'tag_pk': self.pp.tag.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/home/pp_detail.html')

    def test_comment_form_for_auth(self):
        self.client.login(username='test_name', password='1234_5678!')
        resp = self.client.get(reverse('paintsite:detail',
                                       kwargs={'pk': self.pp.pk, 'tag_pk': self.pp.tag.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(type(resp.context['form']) is UserCommentForm)

    def test_comment_form_for_not_auth(self):
        resp = self.client.get(reverse('paintsite:detail',
                                       kwargs={'pk': self.pp.pk, 'tag_pk': self.pp.tag.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(type(resp.context['form']) is GuestCommentForm)


class ProfilePPDetailViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')
        self.client.login(username='test_name', password='1234_5678!')
        self.pp = PictureBoardFactory.create()
        CommentFactory.create(pp=self.pp)
        CommentFactory.create(pp=self.pp)
        CommentFactory.create()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(f'/accounts/profile/{self.pp.pk}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:profile_pp_detail',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:profile_pp_detail',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile/profile_pp_detail.html')

    def test_comment_form(self):
        resp = self.client.get(reverse('paintsite:profile_pp_detail',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(type(resp.context['form']) is UserCommentForm)


class ProfilePPAddViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')
        self.client.login(username='test_name', password='1234_5678!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(f'/accounts/profile/add/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:profile_pp_add'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:profile_pp_add'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile_pp_add.html')


class ProfilePPChangeViewTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')
        self.client.login(username='test_name', password='1234_5678!')
        self.pp = PictureBoardFactory.create()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(f'/accounts/profile/change/{self.pp.pk}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:profile_pp_change',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:profile_pp_change',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile_pp_change.html')


class ProfilePPDeleteTest(TestCase):
    def setUp(self):
        User.objects.create_user('test_name', password='1234_5678!')
        self.client.login(username='test_name', password='1234_5678!')
        self.pp = PictureBoardFactory.create()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(f'/accounts/profile/delete/{self.pp.pk}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('paintsite:profile_pp_delete',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('paintsite:profile_pp_delete',
                                       kwargs={'pk': self.pp.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'paintsite/profile/profile_pp_delete.html')
