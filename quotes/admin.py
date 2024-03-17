from django.contrib import admin

from .models import Tag, Quote, Author

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Quote)
