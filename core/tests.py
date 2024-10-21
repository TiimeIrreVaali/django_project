from django.test import TestCase, Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.character = models.Character.objects.create(
            name='Дзюнко',
            slug='junko',
            type='god',
        )
        self.post = models.News.objects.create(
            title='Проект в разработке!',
            slug='project_indev',
        )

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_character(self):
        response = self.client.get(f'/characters/{self.character.slug}')
        self.assertEqual(response.status_code, 200)

    def test_episodes(self):
        response = self.client.get('/episodes')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.get(f'/posts/{self.post.slug}')
        self.assertEqual(response.status_code, 200)