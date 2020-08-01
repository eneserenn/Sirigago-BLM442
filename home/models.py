from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )

    title = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    description = models.CharField(max_length=110)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=40)
    email = models.CharField(max_length=150)
    smtpserver = models.CharField(max_length=150)
    smptemail = models.CharField(max_length=150)
    smtppassword = models.CharField(max_length=150)
    smtpport = models.CharField(max_length=150)
    icon = models.ImageField(blank =True , upload_to='images/')
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    aboutus = RichTextUploadingField()
    references = RichTextUploadingField()
    contact = RichTextUploadingField()
    status=models.CharField(max_length=10 , choices=STATUS, default="")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title