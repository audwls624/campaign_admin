from django.db import models

class Campaign(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'campaigns'

class CampaignPerDate(models.Model):
    date        = models.DateTimeField()
    reach       = models.IntegerField()
    spend       = models.IntegerField()
    clicks      = models.IntegerField()
    impressions = models.IntegerField()
    installs    = models.IntegerField()
    views       = models.IntegerField()
    ctr         = models.IntegerField()
    campaign    = models.ForeignKey('Campaign', on_delete=models.CASCADE)

    class Meta:
        db_table = 'campaign_per_dates'