import re
from django.urls import path, re_path, reverse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

ALL_URLS = []
if hasattr(settings, 'ACCESS_ALL_URL'):
    ALL_URLS += [re.compile(url) for url in settings.ACCESS_ALL_URL]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        print(path)
        url_is_all = any(url.match(path) for url in ALL_URLS)
        print(url_is_all)

        if path == reverse('accounts:logout').lstrip('/'):
            logout(request)
        
        if url_is_all:
            return None
        else:
            if request.user.is_authenticated and url_is_exempt:
                return redirect(settings.LOGIN_REDIRECT_URL)
            elif request.user.is_authenticated or url_is_exempt:
                return None
            else:
                return redirect(settings.LOGIN_URL)



