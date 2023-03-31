try:
    from django.urls import re_path 
except ImportError:
    from django.conf.urls import url as re_path
try:
    from django.conf.urls import patterns
except ImportError:
    patterns = lambda _, *p: p

from . import views

urlpatterns = patterns("", *[
    re_path(r"^$", views.su_login, name="su-login"),
    re_path(r"^logout$", views.su_logout, name="su-logout"),
])
