from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from icat_cbs import views

# simple url pattern for agent to callback on message state change events
urlpatterns = [
    path('<topic>', views.agent_callback),
]
