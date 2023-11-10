from django.urls import path
from observations.views import test_func

urlpatterns = [
    path('test_func/', test_func)
] 