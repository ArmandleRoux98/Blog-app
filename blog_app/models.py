from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    Represents a Blog post.
    
    Attributes:
        author - Foreign key linked to user account
        title - The title of the post
        body - The content of the post
    """
    author = models.ForeignKey('auth.user', 
                                on_delete=models.CASCADE, 
                                null=True, 
                                blank=True)
    title = models.CharField(max_length=60)
    body = models.TextField()

    def __str__(self) -> str:
        """Returns a string representation of the model."""
        return f"{self.author.username} - {self.title}"