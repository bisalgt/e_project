from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.shortcuts import reverse


from apps.products.models import Product


class User(AbstractUser):
    address = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def _str__(self):
        return self.username

    def get_absolute_url(self):
        data = f"hello {self.username}"
        slug = slugify(data)
        return reverse("user_detail", kwargs={"id": self.id,"slug":slug})



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username


# automatically associate a profile with the user model used by signal post_save
def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
