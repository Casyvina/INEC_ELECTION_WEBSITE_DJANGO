from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class LGA(models.Model):
    id = models.AutoField(primary_key=True)
    lga_id = models.PositiveIntegerField()
    lga_name = models.CharField("lga_name", max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga_description = models.TextField("lga_description")
    entered_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_entered = models.DateTimeField("date_entered", auto_now=True, blank=True)
    user_ip_address = models.GenericIPAddressField("user_ip_address")
    
    def __str__(self):
        return self.lga_name
    
    
class Ward(models.Model):
    id = models.AutoField(primary_key=True)
    ward_id = models.PositiveIntegerField()
    ward_name = models.CharField("ward_name", max_length=50)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    ward_description = models.TextField("ward_description")
    entered_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_entered = models.DateTimeField("date_entered", auto_now=True, blank=True)
    user_ip_address = models.GenericIPAddressField("user_ip_address")
    
    def __str__(self):
        return self.ward_name
    
class PollingUnit(models.Model):
    id = models.AutoField(primary_key=True)
    polling_unit_id = models.PositiveIntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    polling_unit_number = models.CharField("polling_unit_number", max_length=50)
    polling_unit_name = models.CharField("polling_unit_name", max_length=50)
    polling_unit_description = models.TextField("polling_unit_description", null=True)
    lat = models.DecimalField("lat", max_digits=9, decimal_places=6)
    long = models.DecimalField("long", max_digits=9, decimal_places=6)
    entered_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_entered = models.DateTimeField("date_entered", auto_now=True, blank=True)
    user_ip_address = models.GenericIPAddressField("user_ip_address", null=True)

    def __str__(self):
        return self.polling_unit_name
    
class Party(models.Model):
    id = models.AutoField(primary_key=True)
    party_name = models.CharField("name", max_length=100, unique=True)
    party_id = models.CharField("name_abbr", max_length=4, unique=True)
    
    def __str__(self):
        return self.party_name
    
class AnnouncedPuResult(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga = ChainedForeignKey(
        LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    ward = ChainedForeignKey(
        Ward,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    polling_unit = ChainedForeignKey(
        PollingUnit,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False,
        auto_choose=True,
        sort=True
    )

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    entered_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_entered = models.DateTimeField("date_entered", auto_now=True, blank=True)
    user_ip_address = models.GenericIPAddressField("user_ip_address", null=True)
       
    def __str__(self):
        return str(self.id)
    class Meta:
        ordering = ['id']
