from django.db import models
from django.db import models
from django.views.generic import View

# Create your models here.
class ContactUs(models.Model):
    class Meta:
        verbose_name = "ContactUs"
    
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name