from django.shortcuts import redirect
import functools

def custom_login_dec(view_func):
    @functools.wraps(view_func)
    def wrap( request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrap
    
    
