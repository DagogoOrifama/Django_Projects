from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# creating a profile for each user, hence this will extend the user class
# hence the profile and user will be on a oneToOne relationship
class Profile(models.Model):
    # on_delete=models.CASCADE means if a User is deleted, his profile 
    # should also be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # adding a field to the profile model
    # whenever you use imagefield then pillow has to be installed to prevent error
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    # add the string representation of the model
    # enables you to access models in the model
    def __str__(self):
        return self.user.username