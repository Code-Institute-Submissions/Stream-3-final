from django.test import TestCase
from .models import Post

class TestPost(TestCase):

    def test_title(self):
        title_test = Post(title='My Latest Blog Post')
        self.assertEquals(str(title_test), 'My Latest Blog Post')