from django.urls import path
from forms import views
app_name= 'glugforms'
urlpatterns = [
    path('', views.load_index, name='indexloader'),
    path('forms',views.load_home),
    path('editform',views.EditForm),
]