from .models import *

# Create your views here.
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = Profile(nickname=user.username)
        profile.save()
        