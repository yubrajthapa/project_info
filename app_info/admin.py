from django.contrib import admin
#To import selectively
#from . models import StudentDetail, AcademicDetail, TrainingDetail

from .models import *

# Register your models here.
# This will display these fields in admin pannel
# StudentsDetailssAdmin is independent not inherited from anywhere.
class StudentDetailssAdmin(admin.ModelAdmin):
    list_display= ("first_name", "middle_name", "last_name", "email", "contact")
    list_filter = ("first_name", "email", "contact")
    search_fields = ("first_name", "middle_name", "last_name", "email", "contact")

admin.site.register(StudentDetail, StudentDetailssAdmin)
admin.site.register(AcademicDetail)
admin.site.register(TrainingDetail)

# Changing admin page name links title
admin.site.app_index = "Info App"
admin.site.site_header = "Info_App"
admin.site.site_title = "Admin"
admin.site.index_title = "Info App"