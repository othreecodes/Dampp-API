from django.conf.urls import url
from api import views
from rest_framework.compat import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^user/login/$', view=views.login_user, name='login')

]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))

]

urlpatterns = format_suffix_patterns(urlpatterns)
