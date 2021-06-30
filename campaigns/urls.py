from django.urls import path

from campaigns.views import CampaignView

urlpatterns = [
    path('', CampaignView.as_view())
]