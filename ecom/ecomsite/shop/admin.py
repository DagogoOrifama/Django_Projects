from django.contrib import admin
from .models import Products, Order


# customize the admin header
admin.site.site_header = "E-Commerce Site"
# change site title
admin.site.site_title = "Dagoris shopping"
# change the index title in the admin portal
admin.site.index_title = "Manage Dagoris Shopping"

# Specifies which fields of the Products model should be displayed as columns in the list view of the admin interface.
class ProductAdmin(admin.ModelAdmin):
    # define a custom action, this is a custom action to update the category of selected fields
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    # specify searchable fields by specifying the fields
    # make sure to have a comma at the end
    search_fields = ('title','category','description',)
    #in order to modify the action list, specify the method to be in action list in a variable 'actions'
    # ensure to end it with a comma
    actions = ('change_category_to_default',)
    # specify editable fields
    fields = ('title', 'price',)
    # make the fields editable on the list view
    list_editable = ('price', 'category',)

# Register your models here.
# also register the ProductAdmin class along with product to display in list view
admin.site.register(Products, ProductAdmin)
admin.site.register(Order)