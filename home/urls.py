from django.urls import path, include
from . import views
from .views import login_view,admindash,services,collabration,contactus,admincollab


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',login_view,name='Login'),
    path('singup/',views.signup,name='signup'),
    path('register/scholarship', views.scholarships,name='scholarship-registration'),
    path('register/mentorship', views.mentorship,name='mentorship-registration'),
    path('register/englishclasses', views.englishclasses,name='english-registration'),
    path('collabration', views.collabration,name='collabration'),
    path('admin/dashboard',admindash,name='admin-dashboard'),
    path('admin/services',services,name='admin-services'),
    path('admin/collabrations',admincollab,name='admin-collabration'),
    path('admin/contactus', contactus,name='admin-contact'),
]