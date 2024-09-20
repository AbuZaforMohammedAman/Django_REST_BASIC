

# Create your tests here.
'''

from django.test import TestCase
def add(a,b): 
    return a+b

class TestAddTwoValue(TestCase): #Num = 1
    def test_add(self):
        sum = add(10,5)
        print(sum)
        self.assertEqual(sum, 15)

'''

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from status.models import Status
from django.contrib.auth.models import User

class StatusTest(APITestCase):
    def setUp(self):
        new_user = User(username="rakib", password="12345")
        new_user.save()
        status = Status(text="sample test", user= new_user)
        status.save()

    def test_create_account(self):
        url = reverse('status_list_view')
        response = self.client.get(url, format='json')
        print(response.data)
        print(response.status_code)
        status_List = response.data
        self.assertEqual(len(status_List), 1)
        self.assertEqual(response.status_code, 200)
    