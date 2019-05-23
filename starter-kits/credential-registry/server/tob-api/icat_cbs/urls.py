from django.urls import path

from icat_cbs import views


urlpatterns = [
    path('test/<topic>', views.agentCallbackViewset.as_view()),
    path('<topic>', views.agent_callback),
]
