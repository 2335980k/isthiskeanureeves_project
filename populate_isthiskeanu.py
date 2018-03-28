import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isthiskeanureeves_project.settings')

import django
django.setup()

from django.db import models
from isthiskeanureeves.models import Category, Page, UserProfile, User, user_upload
from datetime import datetime
try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.now
#from django.template.defaultfilters import slugify
def populate():
    keanothim = [{"user": "2250052","title": "Not Keanu"}]
    keanew = [{"user": "2250052","title": "Young Keanu"}]
    topkeanu = [{"user": "2250052","title": "Best Keanu"}]
	
    categories = {"topkeanu":{"title": "Top Keanu"},
    "keanew":{"title": "Kea New"},
    "keanothim":{"title": "Kea Not Him"}}

    for category, category_data in  categories.items():
        print("Populating category: " + category_data["title"] )
        c = add_category(category_data["title"])



    users = [
            {"username": "2335980",
             "email": "2335980@student.gla.ac.uk",
             "password": "THisisA63good"
             },
             {"username": "HATEkeanu",
             "email": " angery@me.com ",
             "password": "KeanuSucksHaHa"
             },
             {"username": "Yoshi",
             "email": " blep@toungue.com ",
             "password": "a1234567"
             },
             {"username": "fakekeanu",
             "email": " jamal@hotmal.com",
             "password": "a1234567"
             },
             {"username": "2250052",
             "email": " ",
             "password": "isThisKeanuReeves"
             },
             {"username": "hoya",
             "email": "okkkk@gmail.com ",
             "password": "T3sdif5s"
             },
             {"username": "keanuholic",
             "email": " ",
             "password": "4yyLm40"
             },
             {"username": "testprofile",
             "email": " daftboi@not.com",
             "password": "HailSatanL0L"
             }]

    for user in users:
        
        print("Populating user: " + user['username'])
        u = add_user(user['username'], user['email'], user['password'])

    pages = [
        #{"user": User.id,
        #"image": "2335980k@student.gla.ac.uk",
        #"title": "THisisA63good",
        #"rating" : 40
        #},
        {"user": "HATEkeanu",
        "image": " angery@me.com ",
        "title": "KeanuSucksHaHa",
        "rating" : 30
        },
        {"user": "Yoshi",
        "image": " blep@toungue.com ",
        "title": "a1234567",
        "rating" : 20
        },
        {"user": "fakekeanu",
        "image": " jamal@hotmal.com",
        "title": "a1234567",
        "rating" : 10
        },
        {"user": "2250052",
        "image": " ",
        "title": "isThisKeanuReeves",
        "rating" : 5
        },
        {"user": "hoya",
        "image": "okkkk@gmail.com ",
        "title": "T3sdif5s",
        "rating" : 1
        },
        {"user": "keanuholic",
        "image": " ",
        "title": "4yyLm40",
        "rating" : 0
        },
        {"user": "testprofile",
        "image": " daftboi@not.com",
        "title": "This is a Dog",
        "rating" : 0
        },
        {"user": "testprofile",
        "image": " daftboi@not.com",
        "title": "Haha a cat",
        "rating" : -20
        },
        {"user": "testprofile",
        "image": " daftboi@not.com",
        "title": "Haha a mouse",
        "rating" : -30
        },
        {"user": "testprofile",
        "image": " daftboi@not.com",
        "title": "Big ups",
        "rating" : -11
        }]
           
#    for page in pages:
#        p = add_page(page["user"], "keanew", page["title"],page["image"],page["rating"])
        #p = add_page(page['user'], "keanew", page['title'],page['image'],page['rating'])
        



      
#def add_category(name, image):
def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]#, img=image)[0]
	#c = Category.objects.get_or_create(name=name, img=image)[0]
    #c.rating = rating //OUT
    c.save()
    return c

def add_user(username, email, password):# // populate problem. ############################:
    u = User.objects.get_or_create(username=username,password=password, email=email)[0]
    return u

def add_page(user, category, title, image, rating):
    date = now()
    p = Page.objects.get_or_create(user = user,category = category, title = title,
                                   image = image,date_added = date, rating = rating) [0]
    p.save()
    return p
# Starts execution here
if __name__ == '__main__':
    print("Starting isthiskeanureeves population script...")
    populate()
