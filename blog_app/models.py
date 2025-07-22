from django.db import models

# Create your models here.
class Blog(models.Model):

    author = models.ForeignKey('auth.user', 
                                on_delete=models.CASCADE, 
                                null=True, 
                                blank=True)
    title = models.CharField(max_length=60)
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.author.username} - {self.title}"