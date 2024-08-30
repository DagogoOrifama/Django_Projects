from django.shortcuts import render
from .models import Movies
# to implement pagination
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
    # query the Movie model and return all records
    movie_objects = Movies.objects.all()

    # adding search functionalities
    # move_name - the is the name typed to the input search field in movie_list
    movie_name = request.GET.get('movie_name')

    # check is the search value is valid
    if movie_name != '' and movie_name is not None:
        # # filter the movie name 
        # movie_objects = movie_objects.filter(name=movie_name)
        # filter the movie name by partial matches and case-insensitive search
        # icontains allows for partial matches and case-insensitive search.
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    # split the movies into pages with 4 items per page
    paginator = Paginator(movie_objects, 4)
    # get the current page number
    page = request.GET.get('page')
    # Get the object on that page, this fetches the objects 
    # on the current page and not all the objects
    movie_objects = paginator.get_page(page)

     # Render the movie list template with the paginated movie objects
    return render(request, 'newapp/movie_list.html', {'movie_objects': movie_objects})
