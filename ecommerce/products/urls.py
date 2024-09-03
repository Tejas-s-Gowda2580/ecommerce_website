from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path('account/',views.account,name='account'),
    path('add-to-cart',views.add_to_cart,name='add-to-cart'),
    path('cart',views.cart,name='cart'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
