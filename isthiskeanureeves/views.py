from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from isthiskeanureeves.forms import UserForm, UserProfileForm, CategoryForm, PageForm, EditProfileForm 
from isthiskeanureeves.models import Category, Page, UserProfile
from isthiskeanureeves.get import getUserDetails
from django.contrib.auth.models import User
from isthiskeanureeves.forms import UploadForm
from isthiskeanureeves.models import Upload



def loadContent():
    topKeanu = []
    keaNew = []
    notKeanu = []
    
    for i in Page.objects.all():
        rating = int(i.rating)
        if rating >= 10:
            topKeanu.append(i.title)
            topKeanu.append(str(i.image))
            topKeanu.append(rating)
            topKeanu.append(i.date_added)
        elif rating < 0:
            notKeanu.append(i.title)
            notKeanu.append(str(i.image))
            notKeanu.append(rating)
            notKeanu.append(i.date_added)
        else:
            keaNew.append(i.title)
            keaNew.append(str(i.image))
            keaNew.append(rating)
            keaNew.append(i.date_added)

    pageList = [topKeanu,notKeanu,keaNew]    
    return pageList



# Call index
def index(request):
    page_load_num = 0
    context_dict = {}
    out_list = []
    wrapper_list = []
    lister = loadContent()[page_load_num]
    for i in range(len(lister)):
        if i%4 == 0:
            out_list.append(lister[i])
            out_list.append(lister[i + 1])
            out_list.append(lister[i + 2])
            out_list.append(lister[i + 3])
            if i%12 ==0:
                if i > 4 and i%12 == 0:
                    out_list.append("row")
                    out_list.append("close")
                else:   
                    out_list.append("row")
                flag = True
                    
            wrapper_list.append(out_list)
            print(out_list)
            out_list = []
    #print(wrapper_list)
   
    context_dict = {'items': wrapper_list }

    # Render the response and send it back!
    return render(request, 'isthiskeanureeves/index.html',context_dict)


# Call keanew page	
def keanew(request):
    page_load_num = 2
    context_dict = {}

    out_list = []
    wrapper_list = []
    lister = loadContent()[page_load_num]
    for i in range(len(lister)):
        if i%4 == 0:
            out_list.append(lister[i])
            out_list.append(lister[i + 1])
            out_list.append(lister[i + 2])
            out_list.append(lister[i + 3])
            if i%12 ==0:
                if i > 4 and i%12 == 0:
                    out_list.append("row")
                    out_list.append("close")
                else:   
                    out_list.append("row")
                flag = True
                    
            wrapper_list.append(out_list)
            print(out_list)
            out_list = []
    #print(wrapper_list)
   
    context_dict = {'items': wrapper_list }
    return render(request, 'isthiskeanureeves/keanew.html',context_dict)
# Call about page
def about(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/about.html',context_dict)
    
# Call Kea-not-him page
def keanothim(request):
    page_load_num = 1
    context_dict = {}
    
    out_list = []
    wrapper_list = []
    lister = loadContent()[page_load_num]
    for i in range(len(lister)):
        if i%4 == 0:
            out_list.append(lister[i])
            out_list.append(lister[i + 1])
            out_list.append(lister[i + 2])
            out_list.append(lister[i + 3])
            if i%12 ==0:
                if i > 4 and i%12 == 0:
                    out_list.append("row")
                    out_list.append("close")
                else:   
                    out_list.append("row")
                flag = True
                    
            wrapper_list.append(out_list)
            print(out_list)
            out_list = []
    #print(wrapper_list)
   
    context_dict = {'items': wrapper_list }
    return render(request, 'isthiskeanureeves/notkeanu.html',context_dict)
# Call login page
def login(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/login.html',context_dict)
# Call upload page
def upload(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/upload.html',context_dict)
# Call userprofile
@login_required
def user_profile(request):
    context_dict = {'userProfile' : {}}

    getUser = UserProfile.objects.get(user = request.user)

    # Get all the details of the current logged in user
    context_dict['userProfile'].update(getUserDetails(getUser))

    return render(request, 'isthiskeanureeves/userprofile.html', context_dict)


#Call edit_userfile
@login_required
def edit_userprofile(request):
    # Check if the user exists before edithing their profile
    try:
        user = User.objects.get(username=request.user.username)
    except (User.DoesNotExist) as error:
        print(error)
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    user_form = UserForm(request.POST or None, instance=user)
    profile_form = UserProfileForm(request.POST or None, instance=userprofile)

 
    if user_form.is_valid() and profile_form.is_valid():
       
        user = user_form.save(commit=False)

       
        user.set_password(user.password)
        user.save()

       
        userprofile = profile_form.save(commit=False)
        userprofile.user = user

     
        if 'picture' in request.FILES:
            userprofile.picture = request.FILES['picture']

       
        userprofile.save()

        
        auth_login(request, user)
            
        return render(request, 'isthiskeanureeves/index.html')
    else:
       
        print(user_form.errors, profile_form.errors)
        


    return render(request,
                  'isthiskeanureeves/edit_userprofile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
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

## User upload the picture

def user_upload(request):
    if request.method == 'POST':

        upload_form = UploadForm(request.POST, request.FILES)

        if upload_form.is_valid():

            upload = upload_form.save(commit=False)
            upload.user = request.user
            upload.ratings_id = 0
          

            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()

            return render(request, 'isthiskeanureeves/upload_finish.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.order_by('-date_added')

    return render(request, 'isthiskeanureeves/upload.html',
                  {'uploads': uploads, 'upload_form': upload_form})
