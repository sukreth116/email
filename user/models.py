from django.db import models

# Create your models here.
class country_tb(models.Model):
    countryname=models.CharField(max_length=20)
class state_tb(models.Model):
    statename=models.CharField(max_length=20)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
class user_register_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    stateid=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    security_questions=models.CharField(max_length=20)
    answers=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class hobby_tb(models.Model):
    userid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE)
    hobbyid=models.ForeignKey("siteadmin.hobbyname_tb",on_delete=models.CASCADE)
class message_tb(models.Model):
    senderid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE,related_name="sender")
    receiverid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE,related_name="receiver")
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
    filter_status=models.CharField(max_length=20,default="pending")
class trash_tb(models.Model):
    messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    receiverid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
class contact_tb(models.Model):
    contactid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE,related_name="contact")
    userid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE,related_name="user")
    name=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
class blacklist_tb(models.Model):
    contactid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE,related_name="blacklistedcontact")
    userid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE,related_name="user1")
    name=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
class customer_hobbyfactor_tb(models.Model):
    userid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE)
    hobbyid=models.ForeignKey("siteadmin.hobbyname_tb",on_delete=models.CASCADE)
    factorid=models.ForeignKey("siteadmin.hobbyfactor_tb",on_delete=models.CASCADE)
class customer_agefactor_tb(models.Model):
    userid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey("siteadmin.agefactor_tb",on_delete=models.CASCADE)
class customer_seasoncountry_tb(models.Model):
    userid=models.ForeignKey(user_register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey("siteadmin.seasonfactor_tb",on_delete=models.CASCADE)