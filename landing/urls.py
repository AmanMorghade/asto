from django.urls import path
from .views import home,blog,return_policy,terms_condition,privacy_policy,blog_detail,product_list,add_to_cart,book_appointment,payment_failure,payment_success,cart_list,remove_item

urlpatterns = [
    path('',home,name="home"),
    path('blog',blog,name="blog"),
    path('return',return_policy,name="return_policy"),
    path('terms',terms_condition,name="terms_condition"),
    path('privacy',privacy_policy,name="privacy_policy"),
    path('blog/<int:pk>/', blog_detail, name='detail'),
    path('products/<str:category>/', product_list, name='product_list'),
    path('cart/<int:product_id>/', add_to_cart, name='cart'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-failure/', payment_failure, name='payment_failure'),
    path('cart_list/', cart_list, name='cart_list'),
    path('remove-item/<int:item_id>', remove_item, name='remove_item'),
    
    
]

