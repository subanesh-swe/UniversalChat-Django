from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserAccount(AbstractUser) :
    #phone_number = models.IntegerField(null=True, blank=True)
    userid = models.UUIDField(null=True, blank=True, default=uuid.uuid4)
    userdata = models.JSONField(null=True, blank=True, default=dict)


#import uuid
#from django.contrib.auth.models import AbstractUser
#from django.db import models
#import jsonfield

#class CustomUserModel(AbstractUser):
#    UserId = models.UUIDField(default=uuid.uuid4, editable=False)
    #userdata = models.JSONField(null=True, blank=True, default={})
