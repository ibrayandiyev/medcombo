from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
	pass
admin.site.register(Company, CompanyAdmin)
