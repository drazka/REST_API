from django.contrib import admin

# Register your models here.
from movies.models import Role, Movie, Person

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class MovieAdmin(admin.ModelAdmin):
    pass