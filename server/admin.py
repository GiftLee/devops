from django.contrib import admin
from .models import Host, RemoteUser, RemoteUserBindHost
# Register your models here.

admin.site.site_title = "运维管理系统"
admin.site.site_header = "运维管理系统"
admin.site.index_title = "运维管理系统"


admin.site.register(Host)
admin.site.register(RemoteUser)
admin.site.register(RemoteUserBindHost)
