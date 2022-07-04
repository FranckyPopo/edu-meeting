from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class WelcomeText(models.Model):
    mini_title = models.CharField(
        max_length=150, 
        error_messages={"invalid": "tu et bête comment entre un caratére laba"}
    )
    main_title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)
    
class VideoWelcome(models.Model):
    video = models.FileField() 
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)

class Banner(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)

class MeetingCategory(models.Model):
    name = models.CharField(max_length=150)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)

class Meeting(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField()
    photo = models.ImageField()
    #meeting_category = models.ForeignKey(MeetingCategory, on_delete=models.CASCADE)
    location = models.TextField()
    book_now = models.TextField()
    date_meeting = models.DateTimeField()
    
    monday = models.DateTimeField(blank=True, null=True)
    tuesday = models.DateTimeField(blank=True, null=True)
    Wednesday  = models.DateTimeField(blank=True, null=True)
    Thursday  = models.DateTimeField(blank=True, null=True)
    Friday  = models.DateTimeField(blank=True, null=True)
    saturday = models.DateTimeField(blank=True, null=True)
    sunday = models.DateTimeField(blank=True, null=True)
    
    link_facebbok = models.URLField(blank=True, null=True)
    link_twitter = models.URLField(blank=True, null=True)
    link_instagram = models.URLField(blank=True, null=True)
    link_linkedin = models.URLField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)
    
class BoxBachelor(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField()
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)

class Faq(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)

class PopularCourses(models.Model):
    # faire une recherche sur comment recuperer les etoiles des avis
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    image = models.ImageField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)
    
class UniversityStatistic(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.PositiveIntegerField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)
    
class Video(models.Model):
    url_link_youtube = models.URLField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)
    
class SiteContact(models.Model):
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)
    website = models.URLField()
    _copyright = models.CharField(max_length=150, verbose_name="copyright") 
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.BooleanField(default=True)