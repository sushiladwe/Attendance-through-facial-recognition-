from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
def my_default():
    return {'foo': 'bar'}
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name = "user_profile", on_delete=models.CASCADE, primary_key=True, null = False)
    # description =models.CharField(max_length=100,default=' ')
    # city=models.CharField(max_length=20,default="")
    # phone=models.IntegerField(default=0)
    # head_shot=models.ImageField(upload_to='profil_images',blank=True)
    face_data = models.JSONField(default = my_default)
    
    class Meta:
        
        ordering = ["user"]

    def __str__(self):
        return self.user.username

# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile=UserProfile.objects.get_or_create(user=kwargs['instance'])

# post_save.connect(create_profile,sender=User)