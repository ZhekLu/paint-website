import factory
from faker import Faker

from paintsite.models import User, Tag, PictureBoard, Comment

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    first_name = faker.word()
    last_name = faker.word()
    is_activated = True
    send_messages = True


class SuperTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: 'super_tag_{}'.format(n))
    order = 0
    super_tag = None


class SubTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: 'sub_tag_{}'.format(n))
    order = 0
    super_tag = factory.SubFactory(SuperTagFactory)


class PictureBoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PictureBoard

    tag = factory.SubFactory(SubTagFactory)
    title = faker.sentence(nb_words=4)
    description = faker.sentence()
    image = faker.image_url()
    author = factory.SubFactory(UserFactory)
    is_public = True


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    pp = factory.SubFactory(PictureBoardFactory)
    author = faker.word()
    content = faker.sentence()
