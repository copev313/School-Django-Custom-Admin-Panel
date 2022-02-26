from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True)
    years_studied = models.SmallIntegerField(validators=[
                                                MinValueValidator(0),
                                                MaxValueValidator(19)],
                                             blank=True, default=0)
    courses = models.ManyToManyField('Course',
                                     blank=True,
                                     related_name='students')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=70)
    building = models.CharField(max_length=50)
    office_number = models.CharField(max_length=30)
    degree_type = models.CharField(max_length=60)
    years_tenured = models.SmallIntegerField(validators=[
                                                MinValueValidator(0),
                                                MaxValueValidator(99)])
    courses = models.ManyToManyField('Course',
                                     blank=True,
                                     related_name='instructors')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Course(models.Model):
    name = models.CharField(max_length=70)
    year_taught = models.IntegerField(validators=[MinValueValidator(1900),
                                                  MaxValueValidator(2999)])
    credits = models.SmallIntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(6)])
    course_code = models.CharField(max_length=15,
                                   # unique=True,
                                   default="ABC1234-00")
    grade_type = models.CharField(choices=(
                                        ('G', 'Graded'),
                                        ('U', 'Ungraded'),
                                        ('P', 'Pass/Fail'),
                                        ('E', 'Exam'),
                                    ),
                                    max_length=15,
                                    default='G')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_code} - {self.name} ({self.year_taught})"

    class Meta:
        unique_together = ('name', 'year_taught', )


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(validators=[
                                                MinValueValidator(0),
                                                MaxValueValidator(100)])

    def __str__(self):
        return f"{self.grade}, {self.student}, {self.course}"
