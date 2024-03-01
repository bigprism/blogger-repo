from django import forms

from .models import Post

from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.forms import PasswordResetForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise forms.ValidationError('Content must be at least 10 characters long.')
        return content


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Passwords must match.')
        return password


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Username does not exist.')
        return username


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']
        if password1 != password2:
            raise forms.ValidationError('New passwords must match.')
        return password2


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email Address')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError('Email address does not exist.')
        return email