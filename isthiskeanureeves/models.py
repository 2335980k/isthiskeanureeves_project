from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from star_ratings.models import Rating

#Using for Categoryform
class Category(models.Model):
      name = models.CharField(max_length=128, unique=True)
      slug = models.SlugField(unique=True)
      
      #img = models.CharField(max_length=64, unique=True)

      def save(self, *args, **kwargs):
           self.slug = slugify(self.name)
           super(Category, self).save(*args, **kwargs)

      class Meta:
           verbose_name_plural = 'Categories'

      def __str__(self):
           return self.name
		   
		   
# Sets a file path so that it will go media/<username>/<filename>
def user_upload(instance, filename):
    return 'user_{0}/{1}'.format(instance.user, filename)

# Using for pageform        
class Page(models.Model):
      user = models.ForeignKey(User)
      category = models.ForeignKey(Category)
      title = models.CharField(max_length=128)
      image = models.ImageField(default = "null",upload_to=user_upload)
      date_added = models.DateTimeField(auto_now_add=True)
      rating = models.IntegerField(default = 0)

      def save(self, *args, **kwargs):
           self.slug = slugify(self.title)
           super(Page, self).save(*args, **kwargs)
	  
      def __str__(self): # For Python 2, use __unicode__ too
           return self.title
# Using for UserProfileform
class UserProfile(models.Model):
   
    user = models.OneToOneField(User)
    #username_slug = models.SlugField(unique=True)
    email = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
   # def save(self, *args, **kwargs):
    #    self.username_slug = slugify(self.user.username)
     #   super(UserProfile, self).save(*args, **kwargs)

   
    def __str__(self):
        return self.user.username

# Using for Uploadform
class Upload(models.Model):   
   
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to=user_upload)
    ratings = models.ForeignKey(Rating)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
