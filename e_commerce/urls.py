"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from hello.forms import MypasswordChangeForm,MypasswordResetForm, MysetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('address/',views.address,name='address') ,
    path('product/',views.product,name='product'),
    path('product2/',views.product2,name='product2'),
    path('productdetail/<int:pk>',views.product_detail,name='productdetail'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('showcart/',views.show_cart,name='showcart'),
    path('checkout/',views.check_out,name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
    path('buy-now/',views.buy_now,name='buy-now'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='hello/passwordchange.html',form_class=MypasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='hello/passwordchangedone.html'),name='passwordchangedone'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='hello/password_reset.html',form_class=MypasswordResetForm),name='password_reset'),
    
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='hello/password_reset_done.html'),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='hello/password_reset_confirm.html',form_class=MysetPasswordForm),name='password_reset_confirm'), 
    
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='hello/password_reset_complete.html'),name='password_reset_complete'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
