from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return str(self.caption)


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField()
    excerpt = models.TextField(default="", null=False, blank=True)
    slug = models.SlugField(default="", null=False, blank=True, unique=True)
    content = models.TextField(default="", null=False, blank=True)

    # 1-to-many
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts", null=False
    )

    # many-to-many
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.post_title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
