from django.contrib import admin

from .models import Student, Teacher


class CustomStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'home_group')
    fields = (('name', 'age'), 'home_group')


admin.site.register(Student, CustomStudentAdmin)


class CustomTeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'hire_date')
    fields = (('name', 'age'), 'hire_date')


admin.site.register(Teacher, CustomTeacherAdmin)
