from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import messages
from .forms import StudentForm,MentorshipRegistrationForm,EnglishClassRegistrationForm,CollaborationForm,ContactUsForm,LoginForm
from django.contrib.auth.decorators import login_required
from .models import scholarship, Mentorshipregistration, EnglishClassRegistration, Collaboration, ContactUsSubmission
# Create your views here.


def home(request):
     if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact_us_entry = form.save()

            # You can do additional processing or redirect to another page
            return redirect('home')  # Change 'success-page' to your desired success page

     else:
        form = ContactUsForm()

        context = { 
        'form': form,
     }
        return render(request,'base/home.html',context)

def scholarships(request):
    
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()

    return render(request, 'registration/scholarshipreg.html', {'form': form})


def mentorship(request):
    form = MentorshipRegistrationForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()

    return render(request, 'registration/mentorreg.html', {'form': form})

def englishclasses(request):
    form = EnglishClassRegistrationForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()

    return render(request, 'registration/english.html', {'form': form})

def collabration(request):
    form = CollaborationForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()

    return render(request, 'base/collab.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('admin-dashboard')
            else:
                # Handle invalid login credentials
                # You can customize this part based on your requirements
                messages.error(request, 'Invalid username or password.')

    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})


def signup(request):
    return render(request,'authentication/signup.html')

@login_required
def admindash(request):
    scholarships = scholarship.objects.all()
    scholarship_count = scholarships.count()
    mentorships = Mentorshipregistration.objects.all()
    mentorship_count = mentorships.count()  
    english_classes = EnglishClassRegistration.objects.all()
    english_class_count = english_classes.count()
    collaborations = Collaboration.objects.all()
    collaboration_count = collaborations.count()
    contact_submissions = ContactUsSubmission.objects.all()
    contact_submission_count = contact_submissions.count()
    content = {
        'scholarship_count':scholarship_count,
        'mentorship_count':mentorship_count,
        'english_class_count':english_class_count,
        'collaboration_count':collaboration_count,
        'contact_submission_count':contact_submission_count,
    }
    
    return render(request,'admin/dashboard.html')

@login_required
def services(request):
    scholar = scholarship.objects.all()
    mentor = Mentorshipregistration.objects.all()
    englishclass = EnglishClassRegistration.objects.all()
    content = {
        'scholar': scholar,
        'mentor': mentor,
        'englishclass':englishclass
    }
    
    return render(request,'admin/services.html',content)

@login_required
def admincollab(request):
    collab = Collaboration.objects.all()
    content = {
        'collab':collab
        
    }
    
    return render(request,'admin/collabrations.html',content)

@login_required
def contactus(request):
    contactus = ContactUsSubmission.objects.all()
    content = {
        'contact_responses':contactus,
        
    }
    
    return render(request,'admin/contact.html',content)

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect(reverse('shop:Home')) # Redirect to the home page or any other desired URL after logout