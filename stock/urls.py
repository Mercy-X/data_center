from django.urls import path

from . import views

urlpatterns = [
    path('update_stock_data/', views.update_stock_data, name='update_stock_data'),  # 更新股票信息，ST等
]
