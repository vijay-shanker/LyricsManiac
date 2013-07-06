from account.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget = forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'password']
        exclude = ['last_login', 'is_superuser','groups','user_permissions', 'is_admin', 'is_staff', 'is_active']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def save(self):
        user = super(SignupForm, self).save()
        user.set_password(user.password)
        user.save()
        return user  