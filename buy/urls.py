from django.urls import path
from . import views


urlpatterns = [
    path('<username>/<product_name>',views.buy_products,name='buy_product'),
    path('cart/<username>/',views.cart,name='cart')
]