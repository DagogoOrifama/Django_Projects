# post_save to cos to send signal when user registration is sent
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This function creates a profile when a newly registered user
# $instance - this is the user been saved
# $created holds a boolean value if the user is created or not
# **kwargs -  is a keyword arguement for any addition parameter
# post_save - this tells when the user profile is created, this 
# can be done by adding a receiver as a decorator to the function
# hecnce the function is activated when it received the post_save
# signal from a sender (User)
@receiver(post_save,sender=User)
def build_profile(sender,instance,created, **kwargs):
    # check if user is created
    if created:
        #create profile object
        Profile.objects.create(user=instance)

# This function saves the created profile above
@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()