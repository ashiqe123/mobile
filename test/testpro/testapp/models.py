from django.db import models

# Create your models here.
class test(models.Model):
    brand=models.CharField(max_length=25)
    model=models.CharField(max_length=25)
    type=models.CharField(max_length=10)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.type