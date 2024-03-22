from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

""" 
At the top we import UserCreationForm and UserChangeForm which are used for creating
or updating a user. 
We also import our CustomUser model so that it can be integrated into new
CustomUserCreationForm and CustomUserChangeForm classes.
"""

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'date_of_birth', 'phone_number', 'address', 'gender',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields