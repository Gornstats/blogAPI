from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        
        # Create post
        test_post = Post.objects.create(author=testuser1, title='Blog title', body='Body content goes here')
        test_post.save()
        
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        author = f'{post.author}'
        body = f'{post.body}'
        self.assertEqual(title, 'Blog title')
        self.assertEqual(author, 'testuser1')
        self.assertEqual(body, 'Body content goes here')

    