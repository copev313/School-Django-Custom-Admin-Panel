from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    courses = models.ManyToManyField('Course',
                                     blank=True,
                                     related_name='students')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Course(models.Model):
    name = models.CharField(max_length=70)
    year = models.IntegerField()
    credits = models.IntegerField(validators=[MinValueValidator(1),
                                              MaxValueValidator(5)])
    instructor = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.name}, {self.year}"

    class Meta:
        unique_together = ('name', 'year', )


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,)
    grade = models.PositiveSmallIntegerField(validators=[
                                                MinValueValidator(0),
                                                MaxValueValidator(100)])

    def __str__(self):
        return f"{self.grade}, {self.person}, {self.course}"
