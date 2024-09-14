import random
import string

from attr.validators import max_len
from django.contrib.auth.models import AbstractUser
from django.db.models import (Model,
                              CharField,
                              SlugField,
                              FloatField,
                              TextField,
                              PositiveIntegerField,
                              ForeignKey,
                              CASCADE,
                              DateTimeField, TextChoices, SET_NULL, ImageField)
from django.utils.text import slugify


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        USER = 'user', 'User'

    type = CharField(max_length=10, choices=Type.choices, default=Type.USER)


class SlagBase(Model):
    name = CharField(max_length=50)
    slug = SlugField(max_length=255, editable=False, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            letters = string.ascii_lowercase
            self.slug += ''.join(random.sample(letters, 4))  # 2 - logic
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(SlagBase):
    pass


class Product(SlagBase):
    photo = ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)
    owner = ForeignKey('apps.User', on_delete=SET_NULL, null=True, blank=True)
    price = FloatField()
    description = TextField(null=True, blank=True)
    discount = PositiveIntegerField(default=0)
    category = ForeignKey('apps.Category', on_delete=CASCADE)
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)


class ProductHistory(Model):
    action = CharField(max_length=50, null=True, blank=True)
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    deleted_at = DateTimeField(auto_now_add=True)