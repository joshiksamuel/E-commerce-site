from django.contrib import admin
from esite.models import *
# Register your models here.
admin.site.register(Register)
admin.site.register(Product)
admin.site.register(CartItem)

admin.site.register(shipping)
admin.site.register(Contact)