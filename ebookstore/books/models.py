from django.db import models
from comment_rating.models import CommentRating
from users.models import User

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)


class Category(models.Model):
  category = models.CharField(max_length=50)
  slug = models.SlugField(max_length=100, null=True)


class Publisher(models.Model):
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=20)


class Book(models.Model):
  title = models.CharField(max_length=100)
  synopsis = models.TextField(max_length=500)
  copies_sold = models.IntegerField()
  slug = models.SlugField(max_length=100)
  date = models.DateField(auto_now_add=True)
  image = models.ImageField(upload_to=None)
  pdf = models.FileField(upload_to=None)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)
  author = models.ManyToManyField(Author, on_delete=models.PROTECT)
  publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
  
  
class UserBook(models.Model): 
  #since Django doesn't support composite primary keys,
  #unique_together need to be used ot act as composite primary keys
  class Meta:
      unique_together = ['user_id', 'book_id']

  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
  comment_rating = models.OneToOneField(CommentRating, on_delete=models.CASCADE)
  
  
  


