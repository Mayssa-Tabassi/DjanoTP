from django.urls import path,include
from . import views
from .views import CategoryAPIView,ProduitAPIView


urlpatterns = [
path('', views.index ,name='index'),
path('mesProduit/', views.produit ,name='mesProduit'),
path('majproduit/', views.majproduit ,name='majproduit'),
path('catalogue/', views.catalogue ,name='cataloque'),
path('commande/', views.Commandee ,name='commandee'),
path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
path('cmd/', views.ListCmd ,name='Listcmd'),
path('register/',views.register, name = 'register'), 
path('change-password/',views.change_password, name='change_password'),
path('api/category/', CategoryAPIView.as_view()),
path('api/produits/', ProduitAPIView.as_view())

]