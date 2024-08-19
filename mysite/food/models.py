from django.db import models

# Create your models here.
# model are blueprints to create database tables, they define
# the structure of how the models will be created (eg it defines
# the table columns, names, datatypes, maximum values it can contain, etc)
class Item(models.Model):
    # defining the string representation of the models
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
 