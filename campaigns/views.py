import json

from django.http      import JsonResponse
from django.db.models import Sum
from django.views     import View

from campaigns.models import Campaign, CampaignPerDate

class CampaignView(View):
    def post(self,request):

        try:
            with open('/Users/yangmyeongjin/projects/campaign_admin/campaign_admin/data.json','r') as jsondata:
                data = json.load(jsondata)

            for clm in data["data"]:
                if not Campaign.objects.filter(id=int(clm['campaign_id'])).exists():
                    Campaign.objects.create(id=int(clm['campaign_id']))
                
                date        = clm['start_time'][:10]
                reach       = int(clm.get('reach')) if clm.get('reach') else None
                spend       = int(clm.get('spend')) if clm.get('spend') else None
                clicks      = int(clm.get('clicks')) if clm.get('clicks') else None
                impressions = int(clm.get('impressions')) if clm.get('impressions') else None
                installs    = int(clm.get('installs')) if clm.get('installs') else None
                views       = int(clm.get('views')) if clm.get('views') else None
                campaign_id = int(clm.get('campaign_id'))
                ctr         = clicks/impressions * 100 if (clicks and impressions) else None

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
        
    def get(self,request):
        try:
            start_date = request.GET.get('StartDate')
            end_date   = request.GET.get('EndDate')
            
            if start_date or end_date:                

                campaign_per_dates = CampaignPerDate.objects.filter(date__range=[request.GET['StartDate'],request.GET['EndDate']])            
                indicators         = campaign_per_dates.values('date').annotate(
                    daily_clicks      = Sum('clicks'),
                    daily_impressions = Sum('impressions'),
                    daily_reach       = Sum('reach'),
                    daily_spend       = Sum('spend'),
                    daily_installs    = Sum('installs'),
                    daily_views       = Sum('views'),
                    ctr               = Sum('clicks') / Sum('impressions') * 100
                    )   
                
                result = [
                    {'date'       : indicator_per_day.get('date'),
                    'reach'       : indicator_per_day.get('daily_reach'),
                    'spend'       : indicator_per_day.get('daily_spend'),
                    'clicks'      : indicator_per_day.get('daily_clicks'),
                    'impressions' : indicator_per_day.get('daily_impressions'),
                    'installs'    : indicator_per_day.get('daily_installs'),
                    'views'       : indicator_per_day.get('daily_views'),
                    'ctr'         : indicator_per_day.get('ctr')} for indicator_per_day in indicators]
                
            else:
                campaign_per_dates = CampaignPerDate.objects.all()
                indicators         = campaign_per_dates.aggregate(
                    total_reach       = Sum('reach'),
                    total_spend       = Sum('spend'),
                    total_clicks      = Sum('clicks'),
                    total_impressions = Sum('impressions'),
                    total_installs    = Sum('installs'),
                    total_views       = Sum('views')
                )

                result = {
                    'reach'       : indicators.get('total_reach'),
                    'spend'       : indicators.get('total_spend'),
                    'clicks'      : indicators.get('total_clicks'),
                    'impressions' : indicators.get('total_impressions'),
                    'installs'    : indicators.get('total_installs'),
                    'views'       : indicators.get('total_views'),
                    'ctr'         : indicators.get('total_clicks') / indicators.get('total_impressions') * 100
                    } 
            
            return JsonResponse({'MESSAGE':'SUCCESS', 'RESULTS':result}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE':'NOT_ENOUGH_DATE_INFO'}, status=400)