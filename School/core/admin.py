from django.contrib import admin

from core.models import Course, Grade, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
