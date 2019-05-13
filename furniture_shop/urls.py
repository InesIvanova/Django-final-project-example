from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('furniture/', include('furnitures.urls')),
    path('', include('common.urls'))
]
