from django.db import models

class Books(models.Model):
    class Meta:
        verbose_name = "books"
        verbose_name_plural = "books"
    
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return self.title
