from django.urls import path
from .views import login_view, clients_view, update_status, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('clients/', clients_view, name='clients'),
    path('update_status/<int:client_id>/<str:status>/', update_status, name='update_status'),
    path('logout/', logout_view, name='logout'),
]
