from django.db import models
from django.urls.base import reverse
from django.conf import settings
from django.utils import timezone
class Question(models.Model):
      question_text=models.TextField()
      questionid=models.IntegerField(default=True)
      user=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      created=models.DateField(auto_now_add=True)
      formid=models.IntegerField(default=True)

      def get_absolute_url (self):
            return reverse()


class Choice(models.Model):
      question=models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text=models.CharField(max_length=200)
      user=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Imagefield(models.Model):
      questionimage=models.ForeignKey(Question, on_delete=models.CASCADE)


class ContactFormTemplate(models.Model):
      FormType=models.CharField(max_length=20,default="Personal")
      name=models.CharField(max_length=50)
      EmailAddress=models.EmailField()

# Create your models here.
