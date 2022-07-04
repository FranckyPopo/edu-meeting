from django.contrib import admin

from front import models


@admin.register(models.WelcomeText)
class WelcomeText(admin.ModelAdmin):
    list_display = ["mini_title", "main_title", "date_created", "date_updated"]
    
@admin.register(models.VideoWelcome)
class VideoWelcome(admin.ModelAdmin):
    list_display = ["video", "date_created", "date_updated"]
    
@admin.register(models.Banner)
class Banner(admin.ModelAdmin):
    list_display = ["title", "description", "date_created", "date_updated"]
    
@admin.register(models.MeetingCategory)
class MeetingCategory(admin.ModelAdmin):
    list_display = ["name", "date_created", "date_updated"]
    
@admin.register(models.Meeting)
class Meeting(admin.ModelAdmin):
    list_display = ["name", "price", "date_created", "date_updated"]
    
@admin.register(models.BoxBachelor)
class BoxBachelor(admin.ModelAdmin):
    list_display = ["title", "description", "date_created", "date_updated"]
    
@admin.register(models.Faq)
class Faq(admin.ModelAdmin):
    list_display = ["name", "description", "date_created", "date_updated"]
    
@admin.register(models.PopularCourses)
class PopularCourses(admin.ModelAdmin):
    list_display = ["title", "price", "date_created", "date_updated"]
    
@admin.register(models.Video)
class Video(admin.ModelAdmin):
    list_display = ["url_link_youtube", "video", "date_created", "date_updated"]
    
@admin.register(models.UniversityStatistic)
class UniversityStatistic(admin.ModelAdmin):
    list_display = ["name", "percentage", "date_created", "date_updated"]
    
@admin.register(models.SiteContact)
class SiteContact(admin.ModelAdmin):
    list_display = ["phone", "email", "date_created", "date_updated"]
    
    
