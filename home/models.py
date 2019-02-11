from django.db import models


class HomeSlide(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='homeslide/images')
    link_text = models.CharField(max_length=255)
    link_url = models.URLField(max_length=255)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
