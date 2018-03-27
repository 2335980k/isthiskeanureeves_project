from django.conf.urls import url
from isthiskeanureeves import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'kea-new/$', views.keanew, name='keanew'),
    url(r'about/$', views.about, name='about'),
    url(r'^register/$',views.register, name='register'),
    url(r'kea-not-him/$', views.keanothim, name='keanothim'),
    url(r'login/$', views.user_login, name='login'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'upload/$', views.upload, name='upload'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^userprofile/$', views.user_profile, name='userprofile'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),

    
    ]
