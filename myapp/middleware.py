from staff.views import staff
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.shortcuts import redirect, render
from django.urls import resolve
from myapp.views import checkuser
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        r = resolve(request.path)
        app = r._func_path[:r._func_path.find('.')]
        if app in ["staff",'student']: #add app name IN LIST  to APPLY middleware in that app
            user = checkuser(request)
            if isinstance(user,list):
                if user[0] == app :
                    response = get_response(request)
                else:
                    response = redirect(app+'register')
            else:
                return user
        else:
            response = get_response(request)
        return response
    return middleware