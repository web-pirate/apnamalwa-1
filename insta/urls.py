from django.contrib import admin
from django.urls import path, include
from user import views as user_views

urlpatterns = [
	path('', user_views.index, name='index'),
    path('admin/', admin.site.urls),
]
