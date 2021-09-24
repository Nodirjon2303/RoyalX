from django.db import models


class Reason(models.Model):
    reason = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.id}-sabab"


class Student(models.Model):
    full_name = models.CharField(max_length=150, null=True)
    kasb = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    photo = models.ImageField(null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True)
    job = models.CharField(max_length=120, null=True)
    shior = models.CharField(max_length=125, null=True)
    description = models.TextField(null=True)

    def rasm(self):
        if self.photo != ' ':
            print('photo:', self.photo.path, 'aaaa')
            return 'self.photo'
        else:
            print('photo:', self.photo.path, 'aaaa')
            return 'self.photo'

    def __str__(self):
        return self.full_name


class Reja_teacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    reja = models.CharField(max_length=130, null=True)

    def __str__(self):
        return self.teacher.full_name


class Contact(models.Model):
    telegram = models.CharField(max_length=155, null=True)
    instagram = models.CharField(max_length=155, null=True)
    tiktok = models.CharField(max_length=155, null=True)
    youtube = models.CharField(max_length=155, null=True)
    facebook = models.CharField(max_length=155, null=True)
    mail = models.CharField(max_length=129, null=True)
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.telegram
