from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('itens/', include("itens.urls")),
    path('classes/', include("classes.urls")),
    path('builds/', include("builds.urls")),
]
