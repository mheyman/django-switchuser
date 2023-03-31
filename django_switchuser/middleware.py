import sys

from django.conf import settings as s
from importlib import import_module
from future.utils import raise_with_traceback
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class SuStateMiddleware(MiddlewareMixin):
    su_state_fqcn = getattr(s, "SU_STATE_CLASS", "django_switchuser.state.SuState")
    su_state_module_n, _, su_state_class_n = su_state_fqcn.rpartition(".")
    su_state_module = import_module(su_state_module_n)
    su_state_class = getattr(su_state_module, su_state_class_n)

    def process_request(self, request):
        try:
            request.su_state = self.su_state_class(request)
        except AttributeError as e:
            if not hasattr(request, "user"):
                raise_with_traceback(
                    AttributeError(
                        str(e) + " (NOTE: django_switchuser must be **after** "
                        "django.contrib.auth.middleware.AuthenticationMiddleware!)"
                    ))
            raise
