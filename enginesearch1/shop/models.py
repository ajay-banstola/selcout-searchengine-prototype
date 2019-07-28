from django.db import models
from django.urls import reverse


class Category(models.Model):
    number = models.PositiveIntegerField(null=True, blank=True,default = True)
    name = models.CharField(max_length=150, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(default=0)
    url = models.CharField(max_length=100, default="www.exampleurl.com")

    class Meta:
        ordering = ('-rating',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    number = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, default=True)
   # number = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available = models.NullBooleanField(default=True, null=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        if self.name==None:
         return "ERROR-CUSTOMER NAME IS NULL"
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Mixture(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #available = models.NullBooleanField(default=False, null=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
