from django.contrib import admin
from blogs.models import Contact,Blogs
# Register your models here.

admin.site.register(Contact)

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ["css/main.css"]
        }
        js = ["js/blog.js"]

admin.site.register(Blogs,BlogAdmin)