from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class recipie(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipie_name= models.CharField(max_length=100)
    recipie_description=models.TextField()
    recipie_image=models.ImageField(upload_to="recipie")
    recipie_view_count =models.IntegerField(default=1)
    is_approved = models.BooleanField(default=False)
