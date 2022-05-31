from django.test import TestCase

# Create your tests here.

from paintsite.models import User, SuperTag, Tag, SubTag, Comment, PictureBoard


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(first_name='Big', last_name='Bob',
                            is_activated=True, send_messages=True, username='big_bob')
        User.objects.create(is_activated=True, send_messages=True, username='other')
        Tag.objects.create(name='Super', super_tag=None)
        Tag.objects.create(name='Not', super_tag=Tag.objects.get(name='Super'))
        PictureBoard.objects.create(tag_id=2, title='Post', author=User.objects.get(id=1), is_public=True)
        PictureBoard.objects.create(tag_id=2, title='Post', author=User.objects.get(id=1), is_public=True)
        PictureBoard.objects.create(tag_id=2, title='Post', author=User.objects.get(id=2), is_public=True)
        PictureBoard.objects.create(tag_id=2, title='Post', author=User.objects.get(id=2), is_public=True)

    # Labels Tests

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_user_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_is_activated_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('is_activated').verbose_name
        self.assertEquals(field_label, 'Was activated?')

    def test_send_messages_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('send_messages').verbose_name
        self.assertEquals(field_label, 'Want to get messages about new comments?')

    # Max length

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 150)

    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = User._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 150)

    def test_user_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 150)

    # Other

    def test_object_name_is_username(self):
        user = User.objects.get(id=1)
        expected_object_name = user.username
        self.assertEquals(expected_object_name, str(user))

    def test_get_initial(self):
        user = User.objects.get(username='big_bob')
        self.assertEquals('BI', user.get_initial())

    def test_delete(self):
        user = User.objects.get(username='big_bob')
        posts = PictureBoard.objects.all()
        self.assertEquals(4, posts.count())
        user.delete()
        self.assertEquals(2, posts.count())


class SuperTagManagerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Super', super_tag=None)
        Tag.objects.create(name='Not', super_tag=Tag.objects.get(name='Super'))

    def test_get_queryset(self):
        q = SuperTag.objects.all()
        for tag in q:
            self.assertEquals(tag.super_tag, None)


class SuperTagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Super', super_tag=None)

    def test__str__(self):
        tag = SuperTag.objects.get(id=1)
        self.assertEquals(tag.name, str(tag))


class SubTagManagerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Super', super_tag=None)
        Tag.objects.create(name='Not', super_tag=Tag.objects.get(name='Super'))

    def test_get_queryset(self):
        q = SubTag.objects.all()
        for tag in q:
            self.assertNotEqual(tag, None)


class SubTagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Super', super_tag=None)
        Tag.objects.create(name='Not', super_tag=Tag.objects.get(name='Super'))

    def test__str__(self):
        tag = SubTag.objects.get(name='Not')
        expected_object_name = '%s - %s' % (tag.super_tag.name, tag.name)
        self.assertEquals(expected_object_name, str(tag))


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Super', super_tag=None)
        Tag.objects.create(name='Not', super_tag=Tag.objects.get(name='Super'))
        User.objects.create(username='bob')
        PictureBoard.objects.create(tag_id=1, title='Post', author=User.objects.get(id=1), is_public=True)
        Comment.objects.create(pp_id=1, author='Bob', content='Comment')

    def test__str__(self):
        comment = Comment.objects.get(id=1)
        expected = 'BO'
        self.assertEquals(expected, comment.get_author_initial())
