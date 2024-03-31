from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('celltype/', include(('celltypes.urls', 'celltypes'), namespace='celltypes')),
    path('cellorganelles/', include(('cellorganelles.urls', 'cellorganelles'), namespace='cellorganelles')),
    path('eduprod/', include(('eduprod.urls', 'eduprod'), namespace='eduprod')),
    path('accounts/login/', include('users.urls')),
]