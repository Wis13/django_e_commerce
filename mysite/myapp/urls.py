from django.urls import path
from .views import index, index_item

urlpatterns = [
    path("", index, name='myapp'),
    path("<int:id>/", index_item, name='detail'),
]
