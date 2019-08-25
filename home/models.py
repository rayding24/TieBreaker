from django.db import models

# Create your models here.

class Restaurant(models.Model):
    rest_name = models.CharField(max_length=200)
    rest_add = models.CharField(max_length=1000)
    rest_lat = models.FloatField()
    rest_lon = models.FloatField()
    rest_desc = models.TextField()
    rest_rate = models.FloatField()
    rest_num_review = models.IntegerField()
    rest_avgcost = models.FloatField()

    def createRestaurant(cls, rest_name, rest_lat, rest_lon, rest_desc, rest_rate, rest_num_review, rest_avgcost):
        restaurant = cls(rest_name = rest_name, rest_lat = rest_lat, rest_lon = rest_lon, rest_rate = rest_rate, rest_num_review = rest_num_review, rest_avgcost = rest_avgcost)
        return restaurant