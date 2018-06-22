from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.backends import ModelBackend
from settings import base


def get_user_model():
    """
    Returns the User model that is active in this project.
    """
    try:
        return django_apps.get_model(base.AUTH_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % base.AUTH_USER_MODEL
        )

User = get_user_model()


# Create your views here.
class UserBackend(ModelBackend):
    """

    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.get_obj_or_new(username=username)
            user.save()
            if user.check_password(password):
                return user
        except Exception as e:
            return None
