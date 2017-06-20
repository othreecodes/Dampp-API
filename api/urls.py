from django.conf.urls import url
from rest_framework.compat import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # url(r'^upload/$',views.upload_file,name='upload'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)