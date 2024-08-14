from django import forms
from .models import scholarship,Mentorshipregistration,EnglishClassRegistration,Collaboration,ContactUsSubmission
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, inlineformset_factory, formset_factory


class StudentForm(forms.ModelForm):
    class Meta:
        model = scholarship
        fields = ['first_name', 'last_name', 'email', 'class_name', 'phone_number']

        # You can customize the widgets for each field if needed
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'last_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'email': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': 'email@domain.com'}),
            'class_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'phone_number': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': '123-456-7890'}),
        }



class MentorshipRegistrationForm(forms.ModelForm):
    class Meta:
        model = Mentorshipregistration
        fields = ['first_name', 'last_name', 'class_name', 'email', 'phone_number', 'one_on_one_sessions', 'personalized_guidance', 'skill_development_workshops']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'last_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'class_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'email': forms.EmailInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': 'email@domain.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': '123-456-7890'}),
            'one_on_one_sessions': forms.CheckboxInput(attrs={'class': 'mr-2'}),
            'personalized_guidance': forms.CheckboxInput(attrs={'class': 'mr-2'}),
            'skill_development_workshops': forms.CheckboxInput(attrs={'class': 'mr-2'}),
        }


class EnglishClassRegistrationForm(forms.ModelForm):
    class Meta:
        model = EnglishClassRegistration
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'preferred_time', 'fluency_level']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'last_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'email': forms.EmailInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': 'email@domain.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': '123-456-7890'}),
            'preferred_time': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'fluency_level': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
        }


class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = ['organization_name', 'contact_person_name', 'email', 'phone_number', 'message']

        widgets = {
            'organization_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
            'email': forms.EmailInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': 'email@domain.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50', 'placeholder': '123-456-7890'}),
            'message': forms.Textarea(attrs={'class': 'h-20 border mt-1 rounded px-4 w-full bg-gray-50'}),
        }



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsSubmission
        fields = ['email', 'subject', 'message']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light','placeholder': 'email@domain.com'}),
            'subject': forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light','placeholder': 'Let us know how we can help you'}),
            'message': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500','placeholder': 'leave Your Message...'}),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'inline-block w-full rounded-full bg-white p-2.5 leading-none text-black placeholder-indigo-900 shadow placeholder:opacity-30','placeholder': 'Xyz'})
    )


    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'inline-block w-full rounded-full bg-white p-2.5 leading-none text-black placeholder-indigo-900 shadow placeholder:opacity-30'}),
        label='Password',
        required=True
    )