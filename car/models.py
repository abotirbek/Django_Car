from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100)          # Chevrolet, BMW
    model = models.CharField(max_length=100)          # Malibu, X5
    year = models.PositiveIntegerField()              # 2024
    color = models.CharField(max_length=50)           # Black, White
    price = models.DecimalField(max_digits=12, decimal_places=2)
    mileage = models.PositiveIntegerField()           # bosib o'tgan masofa (km)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"


