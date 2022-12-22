from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Question)
admin.site.register(Answer)