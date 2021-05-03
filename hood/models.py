from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hood_image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_by_location(cls, search_term):
        certain_user=cls.objects.filter(location__icontains=search_term)
        return certain_user
    
    def __str__(self):
        return self.location
class Business(models.Model):
    business_name = models.CharField(max_length=60)
    description = models.CharField(max_length=200) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
