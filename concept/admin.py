from django.contrib import admin
from .models import Programs, Employees, Task, DestinationTask



# Register your models here.


class ProgramAdmin(admin.ModelAdmin):
	fields = ('name',)

class EmployeesAdmin(admin.ModelAdmin):
	fields = ('name','hierarchy','code_number','user_web',)

class TaskAdmin(admin.ModelAdmin):
	fields = ('name','program','requested_employ_id','info',)

class DestinationTaskAdmin(admin.ModelAdmin):
	fields = ('task_id','destination_employ_id')



admin.site.register(Programs, ProgramAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(DestinationTask, DestinationTaskAdmin)