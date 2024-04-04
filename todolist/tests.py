from django.test import TestCase
from .models import TodoItem
from datetime import datetime 
from django.contrib.auth.models import User
# Create your tests here.
# Create your tests here.
class JoinTest(TestCase):   
    
    def test_makeTodo(self):       
                
        user = User.objects.create_user('test_user', password='test_user')
        todo = TodoItem.objects.create(title = 'Schreiben',created_at=datetime.now,author=user,checked=True)        
        # self.client.login(username='munni', password='111abcdefgh')       
        # response = self.client.get('/todos/')            
        # self.assertEqual(response.status_code, 200)
        