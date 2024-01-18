from django.urls import path
from . import views
from .views import animal_list, add_animal, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('animal_list', views.animal_list, name='animal_list'),
    path('animals/', animal_list, name='animal_list'),
    path('animals/add/', add_animal, name='add_animal'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Add LogoutView URL pattern
]
from django.contrib.auth.views import LogoutView

urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
