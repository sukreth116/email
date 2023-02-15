from django.db import models

# Create your models here.
class siteadmin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class hobbyname_tb(models.Model):
    hobby=models.CharField(max_length=20)
class hobbyfactor_tb(models.Model):
    hobbyid=models.ForeignKey(hobbyname_tb,on_delete=models.CASCADE)
    factor=models.CharField(max_length=20)
class season_tb(models.Model):
    season_name=models.CharField(max_length=20)
class seasonfactor_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    seasonfactor=models.CharField(max_length=20)
class seasoncountry_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    countryid=models.ForeignKey("user.country_tb",on_delete=models.CASCADE)
    stateid=models.ForeignKey("user.state_tb",on_delete=models.CASCADE)
    season_factorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    months=models.IntegerField()
class agefactor_tb(models.Model):
    minimum_age=models.IntegerField()
    maximum_age=models.IntegerField()
    age_factor=models.CharField(max_length=20)
