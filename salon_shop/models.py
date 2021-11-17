import uuid 
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        return reverse('salon_shop:style_by_category', args=[self.id])

    def __str__(self):
        return self.name

class Style(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='styles', blank=True)
    time_cost = models.TextField(blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'style'
        verbose_name_plural = 'styles'

    def get_absolute_url(self):
        return reverse('salon_shop:style_detail', args=[self.category.id, self.id])
    
    def __str__(self):
        return self.name