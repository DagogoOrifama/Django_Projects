from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# model are blueprints to create database tables, they define
# the structure of how the models will be created (eg it defines
# the table columns, names, datatypes, maximum values it can contain, etc)
# Also linking the Item Model to the default User model, this can be done 
# by connecting the User model as a foreign key to the Item model
class Item(models.Model):
    # defining the string representation of the models
    def __str__(self):
        return self.item_name
    # user_name is a foreign key on the Item model from the User model
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
 
    # this function tells the app to redirect the user to the item detail page, when a new item is added
    # kwargs (keyword argument) was used to pass in the pk of the added item which was gotten by 'self.pk'
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
