from django.urls import path
from WebApp import views

urlpatterns=[
    path('',views.home_page,name="home"),
    path('about/',views.about_page,name="about"),
    path('contact/',views.contact_page,name="contact"),
    path('products/',views.our_product,name="products"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('products_filtered/<cat_name>/',views.products_filtered,name="products_filtered"),
    path('singleproduct/<int:proid>/',views.singleproduct,name="singleproduct"),
    path('register/',views.register,name="register"),
    path('user_page/',views.user_page,name="user_page"),
    path('save_reg/',views.save_reg,name="save_reg"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_item/<int:pid>/',views.delete_item,name="delete_item")
]