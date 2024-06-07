from django.urls import path
from Backend import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('new_category/',views.new_category,name="new_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('save_page/',views.save_page,name="save_page"),
    path('edit_cat/<int:catid>/',views.edit_cat,name="edit_cat"),
    path('update_cat/<int:catid>/',views.update_cat,name="update_cat"),
    path('delete_cat/<int:catid>/',views.delete_cat,name="delete_cat"),
    path('login_page/', views.login_page, name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('product_page/', views.product_page, name="product_page"),
    path('save_pro/', views.save_pro, name="save_pro"),
    path('display_pro/', views.display_pro, name="display_pro"),
    path('edit_pro/<int:pid>/', views.edit_pro, name="edit_pro"),
    path('update_pro/<int:pid>/', views.update_pro, name="update_pro"),
    path('delete_pro/<int:pid>/', views.delete_pro, name="delete_pro"),


    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact/<int:cid>/',views.delete_contact,name="delete_contact")

]