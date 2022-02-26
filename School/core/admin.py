from dis import Instruction
from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import urlencode
from core.models import Course, Grade, Instructor, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ("year_taught", )
    list_display = ('course_code', 'name', 'year_taught', 'credits', 'instructor', 'view_students')

    def view_students(self, obj):
        from django.utils.html import format_html
        count = obj.students.count()
        url = (
            # Example: "admin:%(app)s_%(model)s_%(page)"
            reverse('admin:core_student_changelist') +
            '?' +
            urlencode({'course__id': f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, count)

    view_students.short_description = "Students"


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_first_name(self):
        if self.cleaned_data["first_name"] == "Spike":
            raise forms.ValidationError("No Vampires")

        return self.cleaned_data["first_name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name", "courses", "years_studied", "date_of_birth")
    form = StudentAdminForm

    list_display = ("last_name", "first_name", "show_average", "years_studied")
    search_fields = ("last_name__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["first_name"].label = "First Name:"
        return form

    def show_average(self, obj):
        from django.db.models import Avg
        from django.utils.html import format_html

        result = Grade.objects.filter(student=obj).aggregate(Avg("grade"))

        return format_html("<b><i>{}</i></b>", result["grade__avg"])

    show_average.short_description = "Grade Average"

    class Meta:
        ordering = ("last_name", "first_name")


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_filter = ("last_name", 'department', )
    list_display = ("last_name", "first_name", "department", )
    search_fields = ("last_name__startswith", )
    
    def view_courses(self, obj):
        from django.utils.html import format_html
        url = (
            # Example: "admin:%(app)s_%(model)s_%(page)"
            reverse('admin:core_instructor_changelist') +
            '?' +
            urlencode({'instructor__id': f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, "Courses")
