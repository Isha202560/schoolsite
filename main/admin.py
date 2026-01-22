from django.contrib import admin
from .models import *

admin.site.register(SchoolInfo)
admin.site.register(Department)
admin.site.register(CampusLife)
admin.site.register(Notice)
admin.site.register(Job)
admin.site.register(AdmissionApplication)   # 👈 ADD THIS
