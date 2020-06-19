from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models her

#class AutoDateTimeField(models.DateTimeField):
#    def pre_save(self, model_instance, add):
#        return timezone.now()

class Post(models.Model):
    quoone = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    seen = models.IntegerField(default=0, editable=False)
    quotwo = models.TextField()
    quothree = models.TextField()  #Change this to multiple choice/autofill option

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering =('-created',)

    def writePost(self, description, source, subject):
        post = self(description=description, source=source, subject=subject)
    



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mentors = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user.username)

