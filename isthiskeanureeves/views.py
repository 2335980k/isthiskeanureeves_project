from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from isthiskeanureeves.forms import UserForm, UserProfileForm, CategoryForm, PageForm
from isthiskeanureeves.models import Category, Page, UserProfile


# Call index
def index(request):
    
    category_list = Category.objects.order_by('-name')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'isthiskeanureeves/index.html',context_dict)
# Call keanuew page	
def keanew(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/keanew.html',context_dict)
# Call about page
def about(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/about.html',context_dict)
    
# Call Kea-not-him page
def keanothim(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/notkeanu.html',context_dict)
# Call login page
def login(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/login.html',context_dict)
# Call upload page
def upload(request):
    return HttpResponse("This is the upload page")
# Call userprofile
@login_required
def user_profile(request):
    context_dict = {}


    return render(request, 'isthiskeanureeves/userprofile.html', context_dict)

#register
def register(request):

       registered = False

       if request.method == 'POST':

            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():

                    user = user_form.save()

                    user.set_password(user.password)
                    user.save()
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    registered = True
                    if 'picture' in request.FILES:
                        profile.picture = request.FILES['picture']
                        profile.save()

                        registered = True
                    else:

                        print(user_form.errors, profile_form.errors)
       else:
           user_form = UserForm()
           profile_form = UserProfileForm()

       return render(request,
                     'isthiskeanureeves/register.html',
                     {'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered})

#login
def user_login(request):
   
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.

        username = request.POST.get('username')
        password = request.POST.get('password')

       
        user = authenticate(username=username, password=password)

       
        if user:
            
            if user.is_active:
            
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
               
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'isthiskeanureeves/login.html', {"message": "Invalid login details. Please try again."})
    else:
      
        return render(request, 'isthiskeanureeves/login.html', {})

# restricted user authentication

@login_required
def restricted(request):
      return render(request, 'isthiskeanureeves/restricted.html', {})

# some view for user status
def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

# logout
@login_required
def user_logout(request):
         logout(request)
         return HttpResponseRedirect(reverse('index'))

# show Category
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        #selects only the uploads of a particular category
        uploads = Upload.objects.filter(category=category)
        context_dict['uploads'] = uploads
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['uploads'] = None
    return render(request, 'isthiskeanureeves/category.html', context_dict)

# add Category
@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.

            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
        
    return render(request, 'isthiskeanureeves/add_category.html', {'form': form})

# add page
@login_required
def add_page(request, category_name_slug):
       try:
            category = Category.objects.get(slug=category_name_slug)
       except Category.DoesNotExist:
            category = None
       form = PageForm()
       if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                  if category:
                      page = form.save(commit=False)
                      page.category = category
                      page.rating = 0
                      page.save()
                      return show_category(request, category_name_slug)
            else:
                  print(form.errors)
       context_dict = {'form':form, 'category': category}
       return render(request, 'isthiskeanureeves/add_page.html', context_dict)

# regiser profile
@login_required
def register_profile(request):
     form = UserProfileForm()
     if request.method == 'POST':
           form = UserProfileForm(request.POST, request.FILES)
           if form.is_valid():
                 user_profile = form.save(commit=False)
                 user_profile.user = request.user
                 user_profile.save()
                 
                 return redirect('index')
           else:
                 print(form.errors)
     context_dict = {'form':form}
     
     return render(request, 'isthiskeanureeves/profile_registration.html', context_dict)
