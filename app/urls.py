
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('verify/', views.verify, name='verify'),
    path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('book/<str:slugName>/', views.book, name='book'),
    path('payment/', views.payment, name='payment'),
    path('update-item/', views.updateItem, name='update-item'),
    path('search/<str:query>/', views.search, name='search'),
    path('api/products/', views.productsApi, name='products-api'),
    path('api/update-account/', views.updateAccount, name='update-account'),
    path('api/user-id/', views.getIdUser, name='user-id'),
    path('api/verify-change-email/', views.verifyChangeEmail, name='verify-change-email'),
    path('api/update-avatar/', views.updateAvatar, name='update-avatar'),
    path('api/change-password/', views.changePassword, name='change-password'),
    path('api/recover-password/', views.recoverPassword, name='recover-password'),
    path('api/verify-recover-password/', views.verifyRecoverPassword, name='verify-recover-password'),
    path('api/recover-success/', views.recoverSuccess, name='recover-success'),
]