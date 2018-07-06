from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from school_management_system.models import School, Student


class SchoolAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'phone_number', 'pin_code', 'email', 'website']
    search_fields = ['name']
    list_filter = ['city']

admin.site.register(School, SchoolAdmin)


class StudentAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['student_name', 'admission_number', 'school', 'class_number', 'date_of_joining']
    search_fields = ['student_name', 'admission_number']
    list_filter = ['school']

admin.site.register(Student, StudentAdmin)
