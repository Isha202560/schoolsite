from django.db import models

class SchoolInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CampusLife(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


# ✅ APPLY NOW MODEL
class AdmissionApplication(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
