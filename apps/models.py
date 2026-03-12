from datetime import date

from django.db.models import Model, ManyToManyField, FileField, ForeignKey, CASCADE
from django.db.models.fields import CharField, DateField, FloatField, TextField


class Course(Model):
    name = CharField(max_length=100)
    price = FloatField()

    class Meta:
        verbose_name_plural = 'courses'

    def __str__(self):
        return f' {self.name}'


class Student(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    phone = CharField(max_length=100)
    birth_date = DateField(default=date.today)
    passport_number = CharField(max_length=100)
    passport_series = CharField(max_length=100)
    course = ManyToManyField('apps.Course', blank=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'



class Document(Model):
    docs =  FileField(upload_to='students/%Y/%m/%d')
    student = ForeignKey('apps.Student', CASCADE)