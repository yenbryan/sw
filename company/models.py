from django.db import models
from registration.models import Profile
from django.template.defaultfilters import slugify


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    founders = models.ManyToManyField(Profile, related_name='companys')
    image = models.ImageField(upload_to='media/company_picture',
                              blank=True,
                              null=True)
    slug = models.CharField(max_length=100, blank=True)
    one_liner = models.CharField(max_length=200, blank=True, null=True)
    backer = models.BigIntegerField(blank=True, null=True, default=0)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Company, self).save(*args, **kwargs)