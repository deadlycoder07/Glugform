from django.urls import path
from forms import views
app_name= 'glugforms'
urlpatterns = [
    path('', views.load_index, name='indexloader'),
    path('forms',views.load_home),
    path('editform',views.EditForm),
    path('form/contactform',views.ContactForm),
    path('form/<slug:slug>/draft',views.show_form,name='show_form'),
    path('form/create',views.create_form,name='create_form'),#customize form view

]