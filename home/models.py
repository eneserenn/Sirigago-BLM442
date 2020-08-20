from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.
from django.forms import ModelForm,TextInput,Textarea

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

class ContactFormMessage(models.Model):
    STATUS = (
        ('New','Yeni'),
        ('Readed','Okundu'),
        ('Answered','Cevaplandı'),
    )

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=110)
    message = models.TextField(max_length=150)
    status=models.CharField(max_length=10 , choices=STATUS, default="")
    ip = models.CharField(max_length=30)
    note = models.CharField(max_length=150 , default="")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name' : TextInput(attrs={'class':'col-lg-12','placeholder': 'Name & Surname'}),
            'subject' : TextInput(attrs={'class':'col-lg-12','placeholder': 'subject'}),
            'email' : TextInput(attrs={'class':'col-lg-12','placeholder': 'email'}),
            'message' : Textarea(attrs={'class':'col-lg-12','placeholder': 'Your Message','rows': '5'}),
        }

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True,max_length=150)
    city = models.CharField(blank=True,max_length=20)
    country = models.CharField(blank=True,max_length=20)
    image = models.ImageField(blank=True,upload_to='images/users/')
    
    def __str__(self):
        return self.user.username
    def user_name(self):
        return '[' +self.user.username +']' + ' '+self.user.first_name+ ' '+self.user.last_name
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','city','country','image']
        