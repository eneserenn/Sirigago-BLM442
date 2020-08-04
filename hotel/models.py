from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    description = models.CharField(max_length=200)
    status=models.CharField(max_length=10 , choices=STATUS, default="")
    slug = models.SlugField()
    parent = TreeForeignKey('self', blank=True,null=True,related_name='children', on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Product(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=200, default="")
    keywords = models.CharField(max_length=200, default="")
    star = models.IntegerField()
    city = models.CharField(max_length=200, default="")
    detail = models.TextField()
    roomtypes = models.CharField(max_length=200, default="")
    price= models.FloatField()
    slug = models.SlugField()
    image = models.ImageField(blank=True,upload_to='images/')
    description = models.CharField(max_length=200, default="")
    status=models.CharField(max_length=10 , choices=STATUS, default="")
    detail = RichTextUploadingField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    hotel = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

