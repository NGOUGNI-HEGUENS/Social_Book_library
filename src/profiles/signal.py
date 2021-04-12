from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profiles, Relationship

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    print(instance, sender, kwargs)
    if created:
        Profiles.objects.create(user=instance)
        
        

@receiver(post_save, sender=Relationship)
def post_save_add_to_friend(sender, instance, created, *args, **kwargs):
    sender_ = instance.receiver
    receiver_ = instance.sender
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()
        
    elif instance.status == 'rejected':
        sender_.friends.remove(receiver_.user)
        receiver_.friends.remove(sender_.user)
        sender_.save()
        receiver_.save()
    