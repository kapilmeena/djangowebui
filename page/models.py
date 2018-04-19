from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=30, null=True)
    page_name = models.CharField(max_length=30, null=True)
    page_content = models.TextField()
    def __str__(self):
        return self.page_name