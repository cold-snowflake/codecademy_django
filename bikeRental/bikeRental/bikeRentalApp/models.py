from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# Create your models here.
class Bike(models.Model):
  STANDART = 'ST'
  TANDEM = "TA"
  ELECTRIC = "EL"
  BIKE_TYPE_CHOICES = [
    (STANDART, 'Standart'),
    (TANDEM, 'Tandem'),
    (ELECTRIC, 'Electric')
  ]
  bike_type = models.CharField(max_length=2, choices=BIKE_TYPE_CHOICES, default=STANDART)
  color = models.CharField(max_length=10, default="")
  def __str__(self):
    return self.bike_type + " - " + self.color
  
class Renter(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=15)
  vip_num = models.IntegerField(default=0) 
  bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
  data = models.DateField(default=datetime.date.today)
  price = models.FloatField(default=0.0)
  def __str__(self):
    return self.first_name + " " + self.last_name + "#" + self.phone
  def calc_price(self):
    curr_price = BASE_PRICE
    if self.bake.bike_type == "TA":
      curr_price += TANDEM_SURCHARGE
    elif self.bike.bike_type == "EL":
      curr_price += ELECTRIC_SURCHARGE
    elif self.renter.vip_num > 0:
      curr_price  = curr_price * 100 / 20 