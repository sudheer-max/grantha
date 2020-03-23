from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Package(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='')
    categories = models.ManyToManyField(Category)
    view_count = models.IntegerField(default=0)
    featured = models.BooleanField()
    content = RichTextUploadingField(default="This is a detail of the pacakges")
    previous_package = models.ForeignKey('self', related_name = 'previous', on_delete= models.SET_NULL, blank=True, null = True)
    next_package = models.ForeignKey('self', related_name = 'next', on_delete = models.SET_NULL, blank=True, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'grantha:blog-detail', kwargs = {
            'id': self.id
        })


class Bus(models.Model):
    thumbnail = models.ImageField(upload_to='')
    bus_name = models.CharField(max_length=100)
    ac_rate = models.IntegerField(default=0)
    non_rate = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    allowance = models.IntegerField(default=0)
    night_allowance = models.IntegerField(default=0)

    def __str__(self):
        return self.bus_name

class Car(models.Model):
    thumbnail = models.ImageField(upload_to='')
    car_name = models.CharField(max_length=100)
    ac_rate = models.IntegerField(default=0)
    extra_person = models.IntegerField(default=0)
    extra_hr = models.IntegerField(default=0)
    night_allowance = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="this is text aboutus writeup")
    thumbnail = models.ImageField(upload_to='')
    featured = models.BooleanField()


    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='')
    comment = models.TextField(default="comment of the clients.")
    featured = models.BooleanField()

    def __str__(self):
        return self.name


class Counter(models.Model):
    number = models.IntegerField(default=0)
    text = models.CharField(max_length=50)
    featured = models.BooleanField()

    def __str__(self):
        return self.text