from django.urls import path
from .views import login_view, success_view, logout_view, rating_view, accountant_orders_view, export_orders_to_excel, supply_history_view, generate_excel_report

urlpatterns = [
    path('', login_view, name='login'),
    path('success/', success_view, name='success'),
    path('logout/', logout_view, name='logout'),
    path('rating/', rating_view, name='rating'),
    path('accounting/', accountant_orders_view, name='accounting'),
    path('supply_history/', supply_history_view, name='supply_history'),
    path('export_orders_excel/', export_orders_to_excel, name='export_orders_excel'),
    path('generate_excel_report/', generate_excel_report, name='generate_excel_report'), 



]
