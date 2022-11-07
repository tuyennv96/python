from django.contrib import admin

# Register your models here.
from .models import Person, Species, Car

admin.site.register(Person)
admin.site.register(Species)
admin.site.register(Car)
