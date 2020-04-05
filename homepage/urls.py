from django.urls import path
from . import views


urlpatterns = [
    path('<username>',views.homepage,name='homepage_log')
]
