from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/<str:title>/', views.entry, name='entry'),
    path('search/', views.search, name='search'),
    path('create/', views.createPage, name='create_page'),
    path('edit/<str:title>/', views.editPage, name='edit_page'),
    path('save/', views.savePage, name='save_page'),
    path('random/', views.randomPage, name="random_page")
]
