from django.test import TestCase
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    #create test string to see if it's storede correctly in database
    def setUp(self):
        Post.objects.create(text='Store this one')
        
    # testing if the text has been stored
    def test_text_content(self):
        post = Post.objects.get(id=1)
        #here object name is the stored string in text variable
        #enclosing our text (string) in a formated string is optional
        #same can be done as 
            #expected_object_name = post.text
        expected_object_name = f'{post.text}'
        #now testing if we have the exact string "store this one"
        self.assertEqual(expected_object_name, 'Store this one')
        
