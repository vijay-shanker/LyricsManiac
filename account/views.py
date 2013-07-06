# Create your views here.
from django import forms
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from account.models import User

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
        
class RegisterView(CreateView):
    template_name = 'register.html'
    model = User
    form_class = SignupForm
    context_object_name = 'form'
    
    def form_valid(self,form ):
        return super(RegisterView,self).form_valid(form)
    
    def get_success_url(self, ):
        return reverse ('bands-list')
    
    

    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render_to_response('login.html', {'form':form},context_instance = RequestContext(request) )
    
    def post(self,request,*args, **kwargs ):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                print "You provided a correct username and password!"
                login(request, user)
                return redirect(reverse('bands-list'))
            else:
                login(request, user)
                print "Your account has been disabled!"
                return redirect(reverse('bands-list'))
        else:
            form = LoginForm()
            return render_to_response('login.html', {'form':form},context_instance = RequestContext(request) )
        
def logout_view(request, next_page):
    logout(request)
    return HttpResponseRedirect(next_page)
    


    
