from django.db import models

# Create your models here.

class Article(models.Model):
    heading = models.TextField()
    para = models.TextField()
    
    def __str__(self):
        return self.heading
    
