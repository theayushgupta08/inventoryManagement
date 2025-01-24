from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('list_products/', views.list_products, name='list_products'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('list_suppliers/', views.list_suppliers, name='list_suppliers'),
    path('add_stock_movement/', views.add_stock_movement, name='add_stock_movement'),
    path('list_stock_movements/', views.list_stock_movements, name='list_stock_movements'),
    path('create_sale_order/', views.create_sale_order, name='create_sale_order'),
    path('list_sale_orders/', views.list_sale_orders, name='list_sale_orders'),
    path('cancel_sale_order/<int:order_id>/', views.cancel_sale_order, name='cancel_sale_order'),
    path('complete_sale_order/<int:order_id>/', views.complete_sale_order, name='complete_sale_order'),
    path('stock_level_check/', views.stock_level_check, name='stock_level_check'),
    path('dashboard/', views.dashboard, name='dashboard')
]