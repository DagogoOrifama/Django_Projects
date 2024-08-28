from . import views
from django.urls import path

# adding namespace
app_name = 'food'
urlpatterns = [
     # for functional-based view
    # path('', views.index, name='index'), #/food/
    # for class-based view (use view_name.as_view())
    path('', views.IndexClassView.as_view(), name='index'), #/food/
    #/food/1
    # path('<int:item_id>/', views.detail, name='detail'),
    # for class-based view
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    # add items
    # path('add/', views.create_item, name='create_item'),
    # modifying url to go with the class-base view
    path('add/', views.CreateItem.as_view(), name='create_item'),
    #edit
    path('update/<int:id>/', views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>/', views.delete_item, name='delete_item')
]
