from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm


# Create your views here.
# def index(request):
#     # Get all the items from the DB
#     item_list = Item.objects.all()
#     # load the html template
#     template = loader.get_template('food/index.html')
#     # the template needs a context, which is the data from the db
#     # the context can be empty.
#     context = {

#     } 
#     # rendering the template by passing the context and request
#     return HttpResponse(template.render(context, request))

# def index(request):
#     # Get all the items from the DB
#     item_list = Item.objects.all()
#     # load the html template
#     template = loader.get_template('food/index.html')
#     # specifying the context
#     context = {
#         'item_list':item_list,
#     } 
#     # rendering the template by passing the context and request
#     return HttpResponse(template.render(context, request))

def index(request):
    # Get all the items from the DB
    item_list = Item.objects.all()
    # specifying the context
    context = {
        'item_list':item_list,
    } 
    # rendering the template by passing the context and request
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse('<h1>This is an item views</h1>')

# This view displays a detail view for each item
def detail(request, item_id):
    # get the item whose primary key is the requested item_id
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

# view to add Items to the database via form 
def create_item(request):
   # create a new form object from the ItemForm form in forms.py
   form = ItemForm(request.POST or None)

   if form.is_valid():
       form.save()
       return redirect('food:index')
   # render a template after creating form
   return render(request, 'food/item-form.html', {'form':form})

# view to update an Item in the database
def update_item(request, id):
    # query the db and get the id of the item to update
    item = Item.objects.get(id=id)
    # create a form object and pass in the data retrieved as instance
    form = ItemForm(request.POST or None, instance=item)

    # validate and save the form, then redirect to home or index page
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    # render the form to the item-form.html template and pass the retrived item
    return render(request, 'food/item-form.html', {'form': form, 'item':item})

# # view to delete an Item to the database 
def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item': item})

    