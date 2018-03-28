from django.contrib import admin
from django.urls import path
from vikinglab.views import HomePage, Pioneer, SomeOneView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('pioneer/<int:user_id>', Pioneer.as_view(), name='viking_pioneer_with_id'),
    path('pioneer/', Pioneer.as_view(),{'user_id':None}, name='viking_pioneer'),
    path('form', SomeOneView.as_view(), name='simple_form'),
    path('admin/', admin.site.urls),
]
