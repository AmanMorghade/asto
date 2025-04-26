from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    image=models.ImageField()
    info=RichTextField()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('gemstone', 'Gemstone'),
        ('rudraksh', 'Rudraksh'),
        ('yantras','Yantras')
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        # return f"{self.name}({self.category})"
        return f"{self.name}"
    

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    service = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    payment_status = models.CharField(max_length=20, default='Pending')
    order_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user_idd = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="cart/")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name