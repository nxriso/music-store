from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/images')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.website


class Guitar(models.Model):
    GUITAR_TYPE_ELECTRIC = 'electric'
    GUITAR_TYPE_ACOUSTIC = 'acoustic'
    GUITAR_TYPE_CHOICES = [
        (GUITAR_TYPE_ELECTRIC, 'Electric'),
        (GUITAR_TYPE_ACOUSTIC, 'Acoustic'),
    ]
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    guitar_type = models.CharField(
        max_length=8,
        choices=GUITAR_TYPE_CHOICES,
        default=GUITAR_TYPE_ELECTRIC,
    )
    djent = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='guitars/images')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '%s - %s' % (self.brand.name, self.model_name)

    def get_absolute_url(self):
        return reverse('show_details', args=(self.brand.name, self.slug))
