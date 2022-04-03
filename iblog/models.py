from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
# Author Model

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    uname = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:36px;height:36px;border-radius:50%;"   />'.format(self.image))

# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    ptitle = models.CharField(max_length=100)
    pcategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    pcontent = HTMLField()
    pdate = models.DateTimeField(auto_now_add=True, null=True)
    purl = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='post/')
    pauthor = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.ptitle

    def pimg_tag(self):
        return format_html('<img src="/media/{}" style="width:36px;height:36px;border-radius:50%;"   />'.format(self.post_img))

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    email_id = models.EmailField()
    username = models.CharField(max_length=100)
    passw = models.CharField(max_length=10)

    def __str__(self):
        return self.fname

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'comment by {self.username} on {self.post}'


