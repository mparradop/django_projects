from django.db import models
from main import models as core

# Create your models here.

class Competitor(models.Model):
    id_competitor = models.AutoField(primary_key=True, db_index=True)
    competitor_name = models.CharField("Name",max_length=100)
    competitor_code = models.CharField("Code",max_length=100)
    description = models.CharField("Description",max_length=100)
    def __str__(self):
        return self.name


class Account(models.Model):
    id_account = models.AutoField(primary_key=True, db_index=True)
    account_name = models.CharField("Name",max_length=100)
    sales_rep = models.ForeignKey(core.Employee, on_delete=models.CASCADE)
    website = models.CharField("Website",max_length=100)
    industry = models.ForeignKey(core.Industry, on_delete=models.CASCADE)
    status = models.ForeignKey(core.Status, on_delete=models.CASCADE)
    region = models.ForeignKey(core.Region, on_delete=models.CASCADE)
    territory = models.ForeignKey(core.Territory, on_delete=models.CASCADE)
    country = models.ForeignKey(core.Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Contact_Role(models.Model):
    role_name = models.CharField("Name",max_length=100)
    description = models.CharField("Description",max_length=100)
    def __str__(self):
        return self.name

class Contact(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField("Name",max_length=100)
    last_name = models.CharField("Last Name",max_length=100)
    role = models.ForeignKey(Contact_Role, on_delete=models.CASCADE)
    email = models.CharField("Email",max_length=100)
    number = models.CharField("Number",max_length=100)

    def __str__(self):
        return self.name


class Leads(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    source = models.ForeignKey(core.Source, on_delete=models.CASCADE)
    persona = models.ForeignKey(Contact, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(core.Product, on_delete=models.CASCADE)
    detail = models.TextField("Detail",max_length=300)
    status = models.ForeignKey(core.Status, on_delete=models.CASCADE)
    next_step = models.TextField("Next Step",max_length=300)
    due_date = models.DateField()

    def __str__(self):
        return self.name


