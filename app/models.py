from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField('Title',max_length=200)
    anons=models.CharField('Anons', max_length=200)
    article_text=models.TextField('Text')
    date=models.DateTimeField('Date')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class Category(models.Model):
    category=models.CharField(max_length=150)