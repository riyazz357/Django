from django.db import models
from django.utils import timezone


# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('PL','PLAIN'),
        ('KL','KIWI'),
        ('EL','ELAICHI'),
        ('GR','GINGER'),
        ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/') #need pillow to use this
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE) #choices for type of chai
    description=models.TextField(default='')

    def __str__(self):
        return self.name
