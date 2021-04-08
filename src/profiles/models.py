from django.db import models
from django.contrib.auth.models import User
from . utils import get_random_code
from  django.template.defaultfilters import slugify

# Create your models here.


class  Profiles(models.Model):
    first_name =     models.CharField(max_length=200, blank=True)
    last_name  =     models.CharField(max_length=200, blank=True)
    user       =     models.OneToOneField(User,  on_delete=models.CASCADE )
    bio        =     models.TextField(default="Enter your bio", max_length=300 )
    email      =     models.EmailField(max_length=200, blank=True )
    country    =     models.CharField(max_length=200, blank=True )
    avatar     =     models.ImageField(default='avatar.png', upload_to='avatars/' )
    
    
    friends    =     models.ManyToManyField(User, blank=True, related_name='friends' )
    slug       =     models.SlugField(unique=True, blank=True)
    update_on  =     models.DateTimeField(auto_now=True )
    create_on  =     models.DateTimeField(auto_now=True )
    
    def __str__(self):
        return f"{self.user.username}-{self.create_on}"
    
    
    def save(self, *args, **kwargs):
        ex =False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            ex = Profiles.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Profiles.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)
