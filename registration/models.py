from django.db import models
from django.contrib.auth.models import AbstractUser
# from company.models import Company


class Profile(AbstractUser):

    COMPANY = 'C'
    BACKER = 'B'
    ADMIN = 'A'

    ACCOUNT_TYPE_CHOICES = (
        (COMPANY, 'company'),
        (BACKER, 'backer'),
        (ADMIN, 'admin'),
    )
    account_type = models.CharField(max_length=1,
                                    choices=ACCOUNT_TYPE_CHOICES,
                                    default=BACKER)

    image = models.CharField(max_length=200, blank=True, null=True)
    one_liner = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    follows = models.ManyToManyField('Profile', related_name='followed_by')
    # follwers = models.ManyToManyField()
    # companys = models.ManyToManyField('Company', related_name='followers')

    """
    Three type of accounts
    Default is BACKER
    """
    def __unicode__(self):
        return self.username


# class Picture(models.Model):
#     image = models.ImageField(upload_to='media/profile_pictures',
#                               blank=True,
#                               null=True)
#     social_image = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=140, blank=True, null=True)
#     # default_picture = models.BooleanField(default=False)
#     profile = models.ForeignKey(Profile, related_name='pictures')
#
#     def __unicode__(self):
#         return 'img{}-{}'.format(self.id, self.profile.username)


# class Interest(models.Model):
#     pass

# class CurrentInvestment(models.Model):
#     pass
#
#
# class Company(models.Model):
#     pass