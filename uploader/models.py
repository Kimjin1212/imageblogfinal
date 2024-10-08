from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded on {self.upload_date}"

# Create your models here.
