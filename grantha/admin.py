from django.contrib import admin
from .models import Package, Category, Bus, Car, About, Testimonial, Counter



admin.site.register(Bus)
admin.site.register(Counter)
admin.site.register(Testimonial)
admin.site.register(About)
admin.site.register(Car)
admin.site.register(Package)
admin.site.register(Category)


