from django.db import models

# Create your models here.
class List(models.Model): #kani kay ang table
         item = models.CharField(max_length=200) #kani sila tong entity sa table
         completed = models.BooleanField(default=False)
         status = ""
         if completed == 2:
                  status = "Ongoing"
         else:
                  status = "Finished"

         def __int__(self):
                  return self.id

class profile(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profile_type = models.CharField(max_length=100, choices = [('Patient','Patient'), ('Employee', 'Employee')], null = True)
    bday = models.DateField(auto_now=False, auto_now_add =False, null = True)
    age = models.IntegerField(null = True)
    deci_number = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)

    def __int__(self):
        return self.id

            

class Contact(models.Model):
         prof_id = models.ForeignKey(profile, on_delete=models.CASCADE, db_constraint = False, default = 1)#
#         prof_id = models.CharField(max_length=1000)
         c_name= models.CharField(max_length=200)
         c_address = models.CharField(max_length=200)
         
         def __str__(self):
                  return self.c_name

class alumni(models.Model):
    firt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_graduated = models.IntegerField(null = True)
    course_graduated = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    current_job = models.CharField(max_length=100)
    current_employer = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True, auto_now_add =True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
