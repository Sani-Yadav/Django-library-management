from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ...existing code...
    path('logout/', views.logout_view, name='logout'),
    # ...existing code...
]