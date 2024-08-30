from django.db import models

# Create your models here.
class Movies(models.Model):
    def __str__(self):
        return self.name
    
    # define string method 
    name = models.CharField(max_length=200)
    rating = models.FloatField()

    # to configure how you want the app to display in the admin portal
    # no migration needed for this
    # class Meta:
    #     verbose_name = "Movie"
    #     verbose_name_plural = "Movies"