from django.contrib import admin
from .models import RemoteLab

# Register your models here.

@admin.register(RemoteLab)
class RemoteLabAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date","Channel1","Channel2","PotValue","acInput1","dcInput1","dcInput2","image"]

    class Meta:
        model = RemoteLab
