from django.urls import path
from . import views
from .views import (HomeView, InputNumView, NewOrderView, ManageOrderView, 
                    ModificationOrderView, AccountingView, AccountingConfirmedView, 
                    AccountingCompletedView, ChangeMenuView, AddMenuView, OrderView, 
                    CheckOrderView, CheckAlreadyOrdered, EditMenuView, UpdateOrderProductView, 
                    OrderConfirmedView, OrderCompletedView, CheckAddedOrderView, AddOrderView, CheckOrderProductCount)

app_name = 'ordering'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('input_table_number/', InputNumView.as_view(), name='input_table_number'),
    path('check_already_ordered/<int:table_number>', CheckAlreadyOrdered.as_view(), name='check_already_ordered'),
    path('new_order/<int:table_number>', NewOrderView.as_view(), name='new_order'),
    path('manage_order/<int:table_number>', ManageOrderView.as_view(), name='manage_order'),
    path('order_list/<int:table_number>', OrderView.as_view(), name='order_list'),
    path('add_order_list/<int:table_number>', AddOrderView.as_view(), name='add_order_list'),
    path('check_order/<int:table_number>', CheckOrderView.as_view(), name='check_order'),
    path('check_added_order/<int:table_number>', CheckAddedOrderView.as_view(), name='check_added_order'),
    path('order_confirmed/<int:table_number>', OrderConfirmedView.as_view(), name='order_confirmed'),
    path('order_completed/<int:table_number>', OrderCompletedView.as_view(), name='order_completed'),
    path('delete_order_product/<int:table_number>/<int:order_product_id>', CheckOrderView.as_view(), name='delete_check_order'),
    path('modification_order/<int:table_number>', ModificationOrderView.as_view(), name='modification_order'),
    path('delete_order_product/<int:table_number>/<int:order_product_id>', CheckOrderView.as_view(), name='delete_modification_order'),
    path('update_order_product/', UpdateOrderProductView.as_view(), name='update_order_product'),
    path('accounting/<int:table_number>', AccountingView.as_view(), name='accounting'),
    path('accounting_confirmed/<int:table_number>', AccountingConfirmedView.as_view(), name='accounting_confirmed'),
    path('accounting_completed/<int:table_number>', AccountingCompletedView.as_view(), name='accounting_completed'),
    path('change_menu/', ChangeMenuView.as_view(), name='change_menu'),
    path('delete_menu/<int:product_id>', views.delete_menu, name='delete_menu'),
    path('add_menu', AddMenuView.as_view(), name='add_menu'),
    path('edit_menu/<int:product_id>', EditMenuView.as_view(), name='edit_menu'),
    path('check_order_product_count/<int:table_number>', CheckOrderProductCount.as_view(), name='check_order_product_count'),
]