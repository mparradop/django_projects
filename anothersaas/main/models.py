from django.db import models

# Create your models here.

class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    country_name = models.CharField(100)
    CCTLD = models.CharField(20)

class Industry(models.Model):
    industry_name = models.CharField(50)

class Company(models.Model):
    company_name = models.CharField(50)
    domain = models.CharField(50)
    address = models.CharField(100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)


class Employee_Role(models.Model):
    role_name = models.CharField(50)
    description = models.CharField(100)

class Employee(models.Model):
    id_emp = models.AutoField(primary_key=True)
    emp_name = models.CharField(40)
    emp_last_name = models.CharField(50)
    user_name = models.CharField(50)

class Org_team(models.Model):
    id_org_team = models.AutoField(primary_key=True)
    team_name = models.CharField(50)
    description = models.CharField(100)

class Org_team_mngr(models.Model):
    id_team_mngr = models.AutoField(primary_key=True)
    id_emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_org_team = models.ForeignKey(Org_team, on_delete=models.CASCADE)

class Region(models.Model):
    region_name = models.Model(30)
    director = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Territory(models.Model):
    territory_name = models.Model(30)
    team_manager = models.ForeignKey(Org_team_mngr, on_delete=models.CASCADE)

