from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static      


urlpatterns = [
    
      path('',views.ProductView.as_view(), name="home"),
      path('details/<int:id>/',views.ProductDetails.as_view(), name="details"),
      path('carts/',views.carts, name="carts"),
      path('shoes/<slug:data>/',views.shoes, name="shoes"),
      path('search/',views.search, name="search"),
      path('registration/',views.RegistrationView.as_view(), name="registration"),
     
      
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
