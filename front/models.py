from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class WelcomeText(models.Model):
    mini_title = models.CharField(max_length=150)
    main_title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)
    
class VideoWelcome(models.Model):
    # faire une recherche sur quell type de champ pour les videos
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)

class Banner(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)

class MeetingCategory(models.Model):
    name = models.CharField(max_length=150)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)

class Meeting(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    date_meeting = models.DateTimeField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)

class Faq(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)

class PopularCourses(models.Model):
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    # faire une recherche sur comment recuperer les etoiles des avis
    image = models.ImageField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)
    
class UniversityStatistic(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.PositiveIntegerField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)
    
class Video(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)
    
class SiteContact(models.Model):
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)
    website = models.URLField()
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=True)