from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Create Model for table Post
class Post(models.Model):
    options = (("draft", "Draft"), ("published", "Published"))

    # Make title with charfield it requires max_length
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=100)
    # slugfield in usable URLfield that does not accept spcial char
    # we can set unique true so each entry is unique
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        # We use User model provided by django
        # Cascade deletes entry from user table on delete
        User,
        on_delete=models.CASCADE,
        related_name="post_author",
    )
    content = models.TextField()
    # auto_now_add only run once
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # auto_now run very time we update
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=options, default="draft"
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        # return human readable text
        return self.title
