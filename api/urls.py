from django.conf.urls import url
from api import views
from rest_framework.compat import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^user/login/$', view=views.login_user, name='login'),
    url(r'^user/matches/$', view=views.Matches.as_view(), name='matches'),
    url(r'^user/suggestions/$', view=views.Suggestions.as_view(), name='suggestions'),
    url(r'^user/create/$', view=views.UserView.as_view(), name='create_user')

]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))

]

urlpatterns = format_suffix_patterns(urlpatterns)
