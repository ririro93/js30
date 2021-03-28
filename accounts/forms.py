from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    # class Meta(UserChangeForm.Meta):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']

class CustomUserCreationForm(UserCreationForm):
    # class Meta(UserCreationForm.Meta):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields