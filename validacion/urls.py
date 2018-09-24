from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

#Este primer url me dice cual vista corresponde a la pagina de inicio!
