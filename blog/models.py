from django.db import models
from django.utils import timezone
<<<<<<< HEAD

=======
>>>>>>> 5a4eed5039ef24126696f1c0d815e0ccfe89f614

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug


class Post(models.Model):
    ACTIVE = "active"
    DRAFT = "draft"

    CHOICES_STATUS = (
        (ACTIVE, "Active"),
        (DRAFT, "Draft")
    )
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    # intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(default =timezone.now)
<<<<<<< HEAD
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
=======
    status = models.CharField(max_length=10, choices=CHOICES_STATUS,default=ACTIVE)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
>>>>>>> 5a4eed5039ef24126696f1c0d815e0ccfe89f614

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
<<<<<<< HEAD
=======


>>>>>>> 5a4eed5039ef24126696f1c0d815e0ccfe89f614
