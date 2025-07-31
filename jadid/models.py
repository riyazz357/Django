from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


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

    def __str__(self): #how this work
        return self.name
    
#one to many c
class chaiReview(models.Model):
    chai=models.ForeignKey(chaiVariety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    #dundor string
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
#many to many relationship
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varities= models.ManyToManyField(chaiVariety,related_name='stores')

    def __str__(self):
        return self.name
    
#one to one relationship

class chaiCertificate(models.Model):
    chai=models.OneToOneField(chaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.name.chai}'
