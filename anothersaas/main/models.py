from django.db import models

# Create your models here.

class Country(models.Model):
    id_country = models.AutoField(primary_key=True, db_index=True)
    country_name = models.CharField("Name",max_length=100)
    CCTLD = models.CharField("CCTLD",max_length=100)

    def __str__(self):
        return self.country_name


class Industry(models.Model):
    industry_name = models.CharField("Name",max_length=100)

    def __str__(self):
        return self.industry_name


class Company(models.Model):
    company_name = models.CharField("Name",max_length=100, )
    domain = models.CharField("Domain",max_length=100)
    address = models.CharField("Address",max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
    

    class Meta:
        verbose_name_plural = "company"


class Category(models.Model):
    id_category = models.AutoField(primary_key=True, db_index=True)
    category_name = models.CharField("Name",max_length=100)
    category_code = models.CharField("Code",max_length=100)
    description = models.CharField("Description",max_length=100)
    
    def __str__(self):
        return self.category_name


class Status(models.Model):
    id_status = models.AutoField(primary_key=True, db_index=True)
    status_name = models.CharField("Name",max_length=100)
    description = models.CharField("Description",max_length=100)
    
    def __str__(self):
        return self.status_name

class Flag(models.Model):
    id_flag = models.AutoField(primary_key=True, db_index=True)
    flag_name = models.CharField("Name",max_length=100)
    description = models.CharField("Description",max_length=100)

class Source(models.Model):
    id_source = models.AutoField(primary_key=True, db_index=True)
    source_name = models.CharField("Name",max_length=100)
    description = models.CharField("Description",max_length=100)

class Risk(models.Model):
    id_risk = models.AutoField(primary_key=True, db_index=True)
    risk_name = models.CharField("Name",max_length=100)
    risk_code = models.CharField("Code",max_length=100)
    description = models.CharField("Description",max_length=100)

class Priority(models.Model):
    id_priority = models.AutoField(primary_key=True, db_index=True)
    priority_name = models.CharField("Name",max_length=100)
    priority_code = models.CharField("Code",max_length=100)
    description = models.CharField("Description",max_length=100)

class Employee_Role(models.Model):
    role_name = models.CharField("Name",max_length=100)
    description = models.CharField("Description",max_length=100)

    def __str__(self):
        return self.role_name


class Employee(models.Model):
    id_emp = models.AutoField(primary_key=True, db_index=True)
    emp_name = models.CharField("Name",max_length=100)
    emp_last_name = models.CharField("Last Name",max_length=100)
    user_name = models.CharField("User name",max_length=100)
    role = models.ForeignKey(Employee_Role, on_delete=models.CASCADE)#,default=0)
    def __str__(self):
        return self.user_name


class Org_team(models.Model):
    id_org_team = models.AutoField(primary_key=True, db_index=True)
    team_name = models.CharField("Name",max_length=100)
    description = models.CharField("Description",max_length=100)


class Org_employee(models.Model):
    id_emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_org_team = models.ForeignKey(Org_team, on_delete=models.CASCADE)


class Org_team_mngr(models.Model):
    id_team_mngr = models.AutoField(primary_key=True, db_index=True)
    id_emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_org_team = models.ForeignKey(Org_team, on_delete=models.CASCADE)


class Region(models.Model):
    region_name = models.CharField("Name",max_length=100)
    director = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Territory(models.Model):
    territory_name = models.CharField("Name",max_length=100)
    team_manager = models.ForeignKey(Org_team_mngr, on_delete=models.CASCADE)


class Product(models.Model):
    id_Product = models.AutoField(primary_key=True, db_index=True)
    product_name = models.CharField("Name",max_length=100)
    product_code = models.CharField("Code",max_length=100)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField("Descriptions",max_length=100)
