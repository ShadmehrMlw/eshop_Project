from django.urls import path
from . import views

urlpatterns = [
    path('', views.userPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('change-password', views.changePasswordPage.as_view(), name='change_password_page'),
    path('edit-profile', views.editUserProfilePage.as_view(), name='edit_profile_page'),
    path('shop-cart', views.user_shop_cart, name='shop_cart_page'),
    path('remove-shop-cart-detail', views.remove_order_content, name='remove_order_cart_detail_ajax'),
    path('change-shop-cart-detail', views.change_order_count, name='change_order_cart_detail_ajax'),
]
