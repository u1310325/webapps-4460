from django.contrib import admin
from .models import Contact

# Register your models here.


from customer_app.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer)
admin.site.register(Contact)