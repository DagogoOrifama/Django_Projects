from django.db import models

# Create your models here.
class Moviedata(models.Model):
    # changing the string representation, this ensures the model shows as its 
    # name in the admin portal and not with 'object'. thats the display name
    # and shows its contents as a list
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    # API endpoint is like creating categorize in the API
    # to do this you need a field to specify categories
    typ = models.CharField(max_length=200, default='action')
    # add image field to model
    # upload_to - defines folder to store the image
    # default - defines the default image name for the image
    image = models.ImageField(upload_to='images/', default="Images/None/NoImg.jpg")