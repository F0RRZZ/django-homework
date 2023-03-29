from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserProfile
        fields = [
            UserProfile.email.field.name,
            UserProfile.first_name.field.name,
            UserProfile.last_name.field.name,
            UserProfile.birthday.field.name,
            UserProfile.image.field.name,
        ]
