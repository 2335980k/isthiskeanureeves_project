from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from population_script import populate
from isthiskeanureeves_project.urls import MyRegistrationView
from isthiskeanureeves.apps import IsthiskeanureevesConfig
from django.apps import apps
from isthiskeanureeves.models import *
from isthiskeanureeves.admin import *
from isthiskeanureeves.forms import *
import os, os.path
from django.template import loader
from django.conf import settings



### generate test for user
def newUser(username):
    user = User.objects.create(username=username)[0]
    user.set_password('testtest')
    user.email = email
    user.save()
    return user


def new_Userprofile(user):
    nprofile = UserProfile.objects.create(user=user, email= 'hola@hotmail.com')
    nprofile.save()
    return nprofile


class AppConfigTests(TestCase):

    def test_isthiskeanureeves_app_config(self):
        self.assertEqual(IsthiskeanureevesConfig.name, 'isthiskeanureeves')
        self.assertEqual(apps.get_app_config('isthiskeanureeves').name, 'isthiskeanureeves')



class iskeanuTest(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)  

    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'isthiskeanureeves/index.html')
    def test_index_contains_link_to_keanew(self):
        
        try:
            response = self.client.get(reverse('index'))
        except:
            try:
                response = self.client.get(reverse('keanew'))
            except:
                return False

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        
    def test_keanew_view(self):
        response = self.client.get(reverse('keanew'))
        self.assertEqual(response.status_code, 200)

    def test_keanothim_view(self):
        response = self.client.get(reverse('keanothim'))
        self.assertEqual(response.status_code, 200)
    
        
    def test_bootstrap_template_exists(self):
      
        path_to_boots = settings.TEMPLATE_DIR + '/isthiskeanureeves/base_boot-strap.html'
        print(path_to_boots)
        self.assertTrue(os.path.isfile(path_to_boots))    

    def test_notlogged(self):
        
        response = self.client.get(reverse('index'))

              
    def test_correct_registration_form(self):
       
        try:
            response = self.client.get(reverse('register_profile'))
        except:
            try:
                response = self.client.get(reverse('register_profile'))
            except:
                return False

     
        self.assertTrue(isinstance(response.context['user_form'], UserForm))

       
        self.assertTrue(isinstance(response.context['profile_form'], UserProfileForm))

        user_form = UserForm()
        profile_form = UserProfileForm()

  
        self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())
        self.assertEquals(response.context['profile_form'].as_p(), profile_form.as_p())

       

    def test_login_Error(self):
        
        try:
            response = self.client.post(reverse('login'), {'username': 'allwrong', 'password': 'hiyahiyas'})
        except:
            try:
                response = self.client.post(reverse('isthiskeanureeves:login'), {'username': 'allwrong', 'password': 'hiyahiyas'})
            except:
                return False


    def test_correct_Login_form(self):
       
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('isthiskeanureeves:login'))
            except:
                return False      
        
    def test_logintohome(self):
        try:
            response = self.client.post(reverse('login'), {'username': 'testing', 'password': 'ajaaja123'})
        except:
            try:
                response = self.client.post(reverse('isthiskeanureeves:login'), {'username': 'testing', 'password': 'ajaaja123'})
            except:
                return False


    def create_user(self):

        user = newUser('holly')
        new_Userprofile(user)
        self.client = Client()

    def test_userprofile_logged(self):
        
        response = self.client.get(reverse('userprofile'))
        self.assertRedirects(response, reverse('auth_login')
        + "?next=/isthiskeanureeves/userprofile/", status_code=302, target_status_code=200)


    def test_userprofile_load(self):
      
        self.client.login(username='holly', password='testtest')
        response = self.client.get(reverse('userprofile'), {'user_id': 'holly'})
        self.assertEqual(response.status_code, 302)

 
    def test_edit_userprofile_load(self):
      
        self.client.login(username='holly', password='testtest')
        response = self.client.get(reverse('edit_userprofile'), {'user_id': 'holly'})
        self.assertEqual(response.status_code, 302)



