from django.urls import path
from django.contrib import admin
from etv import views as v1
from tornado import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v1.index, name='home'),  # Root path now points to the home view
    path('home/', v1.index, name='home'),
    path('quakes/', v1.quakes, name='quakes'),
    path('tsunami/', v1.tsunami, name='tsunami'),
    path('volcano/', v1.volcano, name='volcano'),
    path('tornado/', v2.tornado, name='tornado'),
]

admin.site.site_url = '/home'
