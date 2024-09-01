from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # fetch all the products
    product_objects = Products.objects.all()

    # search functionality - access the input search field and get what is being searched for
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        # filter the products with the search keyword
        # __icontains allows for partial matches and case-insensitive search
        product_objects = product_objects.filter(title__icontains=item_name)

    # Implementing pagination functionality
    # specify the number of products per page
    paginator = Paginator(product_objects, 4)
    # Retrieve the current page number from the URL's query string
    page = request.GET.get('page')
    # Use the paginator.get_page(page) method to get the products for the specified page. 
    # This also handles invalid page numbers and returns the first or last page as needed.
    product_objects = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_objects':product_objects})


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object':product_object})


# View for the checkout page
def checkout(request):
    # check if the checkout form is submited
    if request.method == "POST":
        # get the form data , note the "" signifies they will be empty by default
        items = request.POST.get('items', '')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")

        # create an object to store all the order details
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        # store order the data into the database
        order.save()

    return render(request, 'shop/checkout.html')