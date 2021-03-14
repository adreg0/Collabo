from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

#custom heading on admin
admin.site.site_header = 'Collabro'
admin.site.index_title = 'Admin Dashboard'
admin.site.site_title = 'Collabro'