from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'umair',
            email = 'umair@gmail.com',
            password = 'password'
        )

        self.blog =  Post.objects.create(
            title = 'blog',
            author = self.user,
            body = 'this is blog'
        )

    def test_string_repr(self):
        self.assertEqual(str(self.blog), self.blog.title)

    def test_post_content(self):
        self.assertEqual(f'{self.blog.title}', 'blog')
        self.assertEqual(f'{self.blog.author}', 'umair')
        self.assertEqual(f'{self.blog.body}','this is blog')

    def test_post_list_view(self):
        responce = self.client.get(reverse('home'))
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce,'this is blog')
        self.assertTemplateUsed(responce,'home.html')

    def test_post_detail_view(self):
        responce = self.client.get(reverse('post_detail',  args=[str(self.blog.id)]))
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce,'this is blog')
        self.assertTemplateUsed(responce,'detail.html')
        self.assertEqual(self.client.get('/detail/2/').status_code, 404)

    def test_post_create_view(self):
        responce = self.client.post(reverse('post_new'), {
            'title' : 'blog1',
            'author' : self.user,
            'body' : 'this is blog1',
        })
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, 'this is blog1')
        self.assertContains(responce, 'blog1')
        self.assertTemplateUsed(responce, 'post_create.html')

    def test_post_update_view(self):
        responce = self.client.post(reverse('post_update', args='1'), {
            'title' : 'blog2',
            'body' : 'this is blog1.',
        })
        self.assertEqual(responce.status_code, 302)

        
    def test_post_delete_view(self):
        responce = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'post_delete.html')

