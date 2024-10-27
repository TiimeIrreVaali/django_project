import factory

from django.contrib.auth.models import User

from forum import models


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    email = factory.Faker('email')
    '''
    username = factory.Faker('random_element', elements=[u for u in models.User.objects.all().values_list('username', flat=True).order_by('id')])
    password = factory.Faker('random_element', elements=[p for p in models.User.objects.all().values_list('password', flat=True).order_by('id')])
    email = factory.Faker('random_element', elements=[e for e in models.User.objects.all().values_list('email', flat=True).order_by('id')])
    '''

    class Meta:
        model = User


class SubForumFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('random_element', elements=['News',
                                                      'Characters',
                                                      'Episodes',
                                                      'References',
                                                      'Production',
                                                      'Bugs'])
    slug = factory.Faker('random_element', elements=['news',
                                                     'characters',
                                                     'episodes',
                                                     'references',
                                                     'production',
                                                     'bugs'])

    class Meta:
        model = models.Subforum


class TopicFactory(factory.django.DjangoModelFactory):
    subject = factory.Faker('sentence')
    slug = factory.Faker('slug')
    first_comment = factory.Faker('text')
    created = factory.Faker('date')
    creator = factory.SubFactory(UserFactory)
    subforum = factory.SubFactory(SubForumFactory)

    class Meta:
        model = models.Topic


class CommentFactory(factory.django.DjangoModelFactory):
    #subforum = factory.SubFactory(SubForumFactory)
    topic = factory.SubFactory(TopicFactory)
    author = factory.SubFactory(UserFactory)
    content = factory.Faker('text')
    created = factory.Faker('date')
    pk = factory.Faker('pyint')

    class Meta:
        model = models.Comment
