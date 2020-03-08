from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.mixins import (LoginRequiredMixin, )
from .forms import ContactForm,createform
from django.shortcuts import render, get_object_or_404, redirect
from forms.models import gform
import  string
import  random
import uuid

def rs(string_length=10):
    """Returns a random string of length string_length."""

# Convert UUID format to a Python string.
    random = str(uuid.uuid4())

# Make all characters uppercase.
    random = random.upper()

# Remove the UUID '-'.
    random = random.replace("-","")

# Return the random string.
    return random[0:string_length]

def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
def load_index(request):
    return render(request, 'index.html', {})

def load_home(request):
    user = request.user
    if not user.is_authenticated:
        return  redirect('user:login')
    context={}
    form=gform.objects.filter(user_id=user)
    context['form']=form
    return  render(request,"forms/formshome.html",context)
def EditForm(request):
    return
def ContactForm(request):
    context={}
    if request.method == 'POST':
       form=ContactForm(request.POST)
       if form.is_valid():
           form.save()
           name=form.cleaned_data['name']
           return render(request,"forms/formsubmitted.html",{'name':name})
    else:
        form=ContactForm()
        context['form']=form
        return render(request,"forms/contactform.html",context)


def show_form(request):
    return render(request,"forms/show_form.html",{})

def create_form(request):
    context={}
    user=request.user
    if not user.is_authenticated:
        return  redirect('user:login')
    if request.method=='POST':
        form=createform(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            des=form.cleaned_data['description']
            co=rs(10)
            ob=gform(user_id=user,title=title,description=des,code=co,status="draft")
            ob.save()
            return redirect('/form/{{co}}')
    else:
        form=createform()
        context['form']=form
        return render(request,"forms/create_form.html",context)
