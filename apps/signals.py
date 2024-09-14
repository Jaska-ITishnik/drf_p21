from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from apps.models import Product, ProductHistory


@receiver(post_delete, sender=Product)
def my_callback(sender, instance:Product,  **kwargs):
    ProductHistory.objects.create(action="o'chirildi", name=instance.name, price=instance.price)

@receiver(pre_save, sender=Product)
def save_product_signal(sender, instance: Product, **kwargs):
    pass