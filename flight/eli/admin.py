from django.contrib import admin
from .models import airline, countries, Flights, Customers,Users, UserRoles, airline, Administor, Tickets

# Register your models here.
admin.site.register(countries)
admin.site.register(Flights)
admin.site.register(Customers)
admin.site.register(Users)
admin.site.register(UserRoles)
admin.site.register(airline)
admin.site.register(Administor)
admin.site.register(Tickets)



