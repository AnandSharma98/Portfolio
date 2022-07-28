from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = CloudinaryField('image')  # this is because that media root/ picture is loaded to that
    # location (see this from django portfolio first one from udemy)
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = CloudinaryField('image')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading




# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class workSample(models.Model):  # this is for social handles in about section
    category = models.ForeignKey(Category,
                              on_delete=models.CASCADE)
    icon = CloudinaryField('image')
    link = models.URLField(max_length=200)


class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


# PORTFOLIO SECTION

class Designs(models.Model):
    title = models.CharField(max_length=100, default="NA")
    image =CloudinaryField('image')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Design {self.title}'
