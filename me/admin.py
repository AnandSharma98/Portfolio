from django.contrib import admin

# Register your models here.
from .models import Home, About, workSample, Category, Skills, Designs

# Home
admin.site.register(Home)
admin.site.register(About)


# About

class ProfileInline(admin.TabularInline):  # just another way of registering model
    model = workSample
    extra = 1


# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # category k niche skills
    inlines = [
        SkillsInline, ProfileInline
    ]


# Portfolio
admin.site.register(Designs)
