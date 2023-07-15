from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Item(models.Model):
     category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
     name=models.CharField(max_length=255)
     image = models.ImageField(upload_to='item_image',blank=True, null=True)
     description = models.TextField(blank=True, null=True)
     price = models.FloatField(null=False,blank=False)
     is_Sold = models.BooleanField(default=False)
     create_at = models.DateTimeField(auto_now_add=True)
     created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
     
     def __str__(self):
        return self.name