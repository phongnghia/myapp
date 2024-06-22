from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog-image', null=True)

    class Meta:
        ordering = ['firstName', 'lastName', 'email']

    def __str__(self):
        return self.firstName


class Tag(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    summary = models.TextField()
    createdAt = models.DateField()
    content = models.TextField()

    class Meta:
        ordering = ['title', 'createdAt', 'content']

    def __str__(self):
        return self.title


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)


class PostComment(models.Model):
    content = models.TextField()
