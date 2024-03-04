from django.db import models

# Create your models here.
class Men_latest(models.Model):
    image = models.ImageField(upload_to = "website/images", default="")
    details = models.CharField(max_length = 200)
    # price = models.CharField(max_length = 20)
    def __str__(self):
         return self.details
    
class expanding(models.Model):
    data = models.ForeignKey(Men_latest, on_delete = models.CASCADE)
    price = models.CharField(max_length=50)


