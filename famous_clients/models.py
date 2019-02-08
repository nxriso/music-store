from django.db import models


class FamousClients(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='artists/images')
    quote = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Famous clients"
        ordering = ['order']
