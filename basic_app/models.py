from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    
    # Create relationship (don't inherit from user)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attrubute you want
    portfolio=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute to django.contrib.auth.models.User!
        return self.user.username