from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.mixins import (LoginRequiredMixin, )

def load_index(request):
    return render(request, 'index.html', {})

def load_home(request):
     return  render(request,"forms/formshome.html",{})
def EditForm(request):
    return

