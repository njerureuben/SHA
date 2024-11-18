from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    department = models.CharField(max_length=100)  # To store selected department
    doctor = models.CharField(max_length=100)      # To store selected doctor
    description = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} has Appointment with {self.doctor} on {self.date}"


class Contact(models.Model):
    contactName = models.CharField(max_length=100)
    contactEmail = models.EmailField()
    contactSubject = models.CharField(max_length=15)
    contactMessage = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.contactName}"
