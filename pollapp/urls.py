from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('registrations/',views.registrations),
    path('handlelogin/',views.handlelogin),
    path('handlelogout/',views.handlelogout),
    path('contact/',views.contact),
    path('dashboard/',views.dashboard),
    path('detail/<int:id>',views.detail),
    path('create/',views.detail),
    path('save_exist/<int:id>',views.save),
    path('save/',views.save),
    path('donate/',views.donate),
    path('share/<int:id>',views.share),
    path('delete/<int:id>',views.delete),
    path('votecount/<int:id>',views.votecount),
    path('search/',views.search),
    
]