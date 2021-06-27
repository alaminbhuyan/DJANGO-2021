from .models import Status
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Status)
def delete_related_user(sender, instance, **kwargs):
    print("Page post deleted successfully") # for understanding purpose
    instance.user.delete()