from django.db import models
from django.urls.base import reverse
from django.conf import settings
from django.utils import timezone
class gform(models.Model):
      user_id=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title=models.CharField(max_length=200)
      description=models.TextField(default='')
      code=models.SlugField(max_length=250,unique=True)
      status=models.CharField(max_length=20)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      def __str__(self):
            return self.title
class form_field(models.Model):
      form_id=models.ForeignKey(gform,on_delete=models.CASCADE)
      template=models.CharField(max_length=190)
      attribute=models.CharField(max_length=200)
      question=models.CharField(max_length=400,null=True)
      required=models.BooleanField(null=True)
      options=models.TextField(null=True)
      filled=models.BooleanField(null=True)
      created_at = models.DateTimeField(auto_now_add=True,null=True)
      updated_at = models.DateTimeField(auto_now=True,null=True)

class form_response(models.Model):
      form_id = models.ForeignKey(gform, on_delete=models.CASCADE)
      field_id= models.ForeignKey(form_field, on_delete=models.CASCADE)
      answer=models.TextField(null=True)
      created_at = models.DateTimeField(auto_now_add=True, null=True)
      updated_at = models.DateTimeField(auto_now=True, null=True)

class modify_form_responses(models.Model):
      form_id=models.ForeignKey(gform,on_delete=models.CASCADE)
      response_code=models.CharField(max_length=190)
      respondent_ip=models.GenericIPAddressField()
      respondent_user_agent=models.CharField(max_length=190)




class ContactFormTemplate(models.Model):
      FormType=models.CharField(max_length=20,default="Personal")
      name=models.CharField(max_length=50)
      EmailAddress=models.EmailField(default='')
      Address=models.TextField(default='')
      ContactNumber=models.IntegerField(default='')

# Create your models here.
