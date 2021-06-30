import json

from django.http  import JsonResponse
from django.views import View

from campaigns.models import Campaign, CampaignPerDate

class CampaignView(View):
    def post(self,request):

        try:
            with open('/Users/yangmyeongjin/projects/campaign_admin/campaign_admin/data.json','r') as jsondata:
                data=json.load(jsondata)

            for clm in data["data"]:
                if not Campaign.objects.filter(id=int(clm['campaign_id'])).exists():
                    Campaign.objects.create(id=int(clm['campaign_id']))
                
                date = clm['start_time'][:10]
                reach       = int(clm.get('reach')) if clm.get('reach') else None
                spend       = int(clm.get('spend')) if clm.get('spend') else None
                clicks      = int(clm.get('clicks')) if clm.get('clicks') else None
                impressions = int(clm.get('impressions')) if clm.get('impressions') else None
                installs    = int(clm.get('installs')) if clm.get('installs') else None
                views       = int(clm.get('views')) if clm.get('views') else None
                campaign_id = int(clm.get('campaign_id'))
                ctr         = clicks/impressions * 100 if (clicks and impressions) is not None else None

                CampaignPerDate.objects.create(
                    date        = date,
                    reach       = reach,
                    spend       = spend,
                    clicks      = clicks,
                    impressions = impressions,
                    installs    = installs,
                    views       = views,
                    ctr         = ctr,
                    campaign_id = campaign_id
                    )
            
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=401)
        
    # def get(self,request):       