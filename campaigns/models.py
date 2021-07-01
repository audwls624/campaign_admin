from django.db import models

class Campaign(models.Model):
    id           = models.BigIntegerField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'campaigns'

class CampaignPerDate(models.Model):
    date        = models.DateField(null=True)
    reach       = models.IntegerField(null=True)
    spend       = models.IntegerField(null=True)
    clicks      = models.IntegerField(null=True)
    impressions = models.IntegerField(null=True)
    installs    = models.IntegerField(null=True)
    views       = models.IntegerField(null=True)
    ctr         = models.IntegerField(null=True)
    campaign    = models.ForeignKey('Campaign', on_delete=models.CASCADE)

    class Meta:
        db_table = 'campaign_per_dates'