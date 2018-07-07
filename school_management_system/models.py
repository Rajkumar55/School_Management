from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    pin_code = models.CharField(max_length=6, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False, help_text='Phone number with STD code')
    email = models.EmailField(max_length=50, null=True, blank=True)
    website = models.URLField(help_text='Link to the website', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'school'


class Student(models.Model):
    student_name = models.CharField(max_length=100, null=False, blank=False)
    admission_number = models.IntegerField(null=False, blank=False, unique=True)
    address = models.TextField(null=False, blank=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=False, blank=False)
    class_number = models.IntegerField(null=False, blank=False, help_text='In which class the student is enrolled')
    date_of_joining = models.DateField(auto_now_add=True)
    emergency_contact_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'student'
