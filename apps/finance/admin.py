from django.contrib import admin
from .models import Receipt
from .models import Invoice
from .models import InvoiceItem


# Register your models here.

admin.site.register(Receipt)