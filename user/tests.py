from django.test import TestCase

# Create your tests here.
from user.models import CustomUser


class TestUserModel(TestCase):
    """ """
    
    def setUp(self):
        """ """
        user = CustomUser.object.create(username='Usertest', email='test@test.fr', password='motdepasse445')
        user.save()
    
    
    def test_user_model(self):
        """ """
        user_test = CustomUser.object.get(username='Usertest')
        self.assertEqual(user_test.username, 'Usertest')