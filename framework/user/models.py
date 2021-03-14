from django.db import models
from django.contrib.auth.models import AbstractUser
from framework.utils import GENDER_CHOICES

class User(AbstractUser):
    
    id = models.BigAutoField(primary_key=True, null=False)
    # email address of the organization
    email = models.EmailField(unique=True, null=True, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # varchar(255), Organization's name
    first_name = models.CharField(max_length=255, default='', blank=False, verbose_name='First Name/Org Name')
    last_name = models.CharField(max_length=255, default='', blank=True, verbose_name='Last Name')
    # varchar(255), a short self-written bio of the organization that will be shown in the org profile
    motives = models.CharField(max_length=255, default='', blank=True, verbose_name='Goals and Motives')
    # The Tech Stacks that the organization uses
    tech = models.CharField(max_length=255, default='', blank=True, verbose_name='Tech Stack')
    # The Organization URL
    org_url = models.URLField(max_length=200, null=True, verbose_name="Organization URL")
    # The Projects handled by the organization
    projects = models.CharField(max_length=255, default='', blank=True, verbose_name='Organization Projects')
    # The Status decided whether the org is looking for contributors or if the user is looking to contribute
    status = models.CharField(
        max_length=50,
        choices=(("1",'Looking for contributors'),("2",'Looking to contribute')),
        default='1'
    )
    # Demographic Data
    birthday = models.DateField(null=True, blank=True)
    # gender of the user, should not be shown publicly on profile
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True,  blank=True)
    # residence location of the user
    city = models.CharField(max_length=127, default='', blank=True)
    state = models.CharField(max_length=127, default='', blank=True)
    country = models.CharField(max_length=10, null=True, blank=False, default='IND')