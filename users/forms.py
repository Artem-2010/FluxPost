from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 outline-none transition-all'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 outline-none transition-all'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'w-full px-4 py-2 text-sm file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 cursor-pointer'}),
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-300 focus:border-blue-500 focus:ring-2 outline-none transition-all'})
        }
