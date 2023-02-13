from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from posts.models import Group, Post

User = get_user_model()


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = User.objects.create(username='authtest')
        cls.group = Group.objects.create(
            title='Тестовый заголовок группы',
            slug='test_slug',
            description='Тестовое описание группы',)
        cls.post = Post.objects.create(
            text='Текст поста',
            author=cls.author,
            group=cls.group,
        )

    def setUp(self):
        self.guest_client = Client()
        self.author = User.objects.get(username='authtest')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.author)

    def test_home(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_createAuth_url(self):
        """Страница /create/ доступна авторизованному пользователю."""
        response = self.authorized_client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_groupSlug_url(self):
        """Страница /group/<slug>/ доступна любому пользователю."""
        response = self.guest_client.get(f'/group/{self.group.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        """Страница /pofile/<username>/ доступна любому пользователю."""
        response = self.guest_client.get('/profile/authtest/')
        self.assertEqual(response.status_code, 200)

    def test_postid_url(self):
        """Страница /posts/<post_id>/"""
        """Доступна любому пользователю."""
        response = self.guest_client.get(f'/posts/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_postid_url(self):
        """Страница /posts/<post_id>/edit/"""
        """Доступна автору поста."""
        response = self.authorized_client.get(f'/posts/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_unexisting_page(self):
        """Страница /unexisting_page/ не существует."""
        response = self.guest_client.get('/unexisting_page/')
        self.assertEquals(response.status_code, 404)
