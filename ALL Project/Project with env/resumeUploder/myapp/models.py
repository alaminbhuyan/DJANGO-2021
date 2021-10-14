from django.db import models

# Create your models here.

STATE_CHOICE     = (
    ('Dhaka North', 'Dhaka North'),
    ('Dhaka South', 'Dhaka South'),
    ('Chittagong', 'Chittagong'),
    ('Gazipur', 'Gazipur'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Mymensingh', 'Mymensingh'),
    ('Sylhet', 'Sylhet'),
    ('Comilla', 'Comilla'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
    ('Narayanganj', 'Narayanganj'),
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=80)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=70)
    profile_image = models.ImageField(upload_to="profileImg", blank=True)
    my_files = models.FileField(upload_to="doc", blank=True)