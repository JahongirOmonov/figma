from django.contrib import admin
from .models import bookModel
from .models import authorModel

# Register your models here.

admin.site.register(bookModel)
admin.site.register(authorModel)
