from django import forms
from django.contrib.auth.models import User
from isthiskeanureeves.models import Category, UserProfile, Page

# Category form
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    #img = forms.CharField(max_length=64, unique=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)
## page forms
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

       
        exclude = ('category',)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = ('http://') + url
            cleaned_data['url'] = url

            return cleaned_data
# User registration form1
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# User registration form2
class UserProfileForm(forms.ModelForm):
    
    #email = forms.URLField(required=False)
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ('picture',)
# User profile edit form
class EditProfileForm(forms.ModelForm):
    

    class Meta:
        model = UserProfile
        fields = ('picture',)
        exclude = ('username','password','email')

   

#class UploadForm(forms.ModelForm):
   # class Meta:
    #    model = Upload
     #   fields = ('name', 'picture', 'category')
