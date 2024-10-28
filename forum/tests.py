from django.test import TestCase
from django.urls import reverse

from forum import factories, models
from forum.models import Topic, Comment
from forum.views import TopicListView


class SubforumTestCase(TestCase):
    def setUp(self):
        self.subforum = factories.SubForumFactory()
        self.user = factories.UserFactory()
        self.topic = factories.TopicFactory(subforum=self.subforum, creator=self.user)

    def test_get_topic_list(self):
        url = reverse('forum:subforum', kwargs={'subforum_slug': self.subforum.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['topics'].count(), models.Topic.objects.count())

    def test_get_topic_detail(self):
        url = reverse("forum:topic", kwargs={'subforum_slug': self.subforum.slug, 'topic_slug': self.topic.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/topic.html")


class CommentTestCase(TestCase):
    def setUp(self):
        self.subforum = factories.SubForumFactory()
        self.user = factories.UserFactory()
        self.topic = factories.TopicFactory(subforum=self.subforum, creator=self.user)
        self.comment = factories.CommentFactory(topic=self.topic, author=self.user)
        self.client.force_login(self.user)

    def test_add_comment(self):
        data = {
            'content': self.comment.content
        }
        url = reverse("forum:add_comment", kwargs={
            'subforum_slug': self.topic.subforum.slug,
            'topic_slug': self.topic.slug
        })
        old_comments_count = Comment.objects.count()
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertGreater(Comment.objects.count(), old_comments_count)

    def test_update_comment(self):
        data = {
            'content': 'hehehehehehehe'
        }
        url = reverse("forum:edit_comment", kwargs={
            'subforum_slug': self.topic.subforum.slug,
            'topic_slug': self.topic.slug,
            'pk': self.comment.pk
        })
        old_content = self.comment.content
        response = self.client.post(url, data=data)
        self.comment.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.comment.content, old_content)

    def test_delete_comment(self):
        url = reverse("forum:delete_comment", kwargs={
            'subforum_slug': self.topic.subforum.slug,
            'topic_slug': self.topic.slug,
            'pk': self.comment.pk
        })
        old_comments_count = Comment.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_comments_count, Comment.objects.count())
