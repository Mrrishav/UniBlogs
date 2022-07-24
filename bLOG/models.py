from django.db import models

# Create your models here.
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# from tinymce.models import HTMLField

User = get_user_model()


class Category(models.Model):
    cat_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    def image_tag(self):
        return format_html('<img scr="/media/{}" style="width:40px;height:40px;border-radius:50%"/>'.format(self.image))


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.user.username





class Post(models.Model):
    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    likes = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img scr="/media/{}" style="width:40px;height:40px;border-radius:50%"/>'.format(self.image))

