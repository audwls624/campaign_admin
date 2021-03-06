import json


sample_data = { 
    "data" :[
{
 "start_time": "2020-01-20T15:26:17+0900",
 "end_time": "2020-01-20T15:26:17+0900",
 "reach": "234535",
 "spend": "55438",
 "clicks": "3655",
 "impressions": 62746,
 "installs": 2342,
 "views": 2834,
 "campaign_id": "287634828273"
},
{
 "start_time": "2020-01-21T15:26:17+0900",
 "end_time": "2020-01-21T15:26:17+0900",
 "reach": 3674643,
 "spend": 72633,
 "clicks": "3823",
 "installs": "3812",
 "views": 3674,
 "campaign_id": "287634828273"
},
{
 "start_time": "2020-01-22T15:26:17+0900",
 "end_time": "2020-01-22T15:26:17+0900",
 "reach": 423671,
 "spend": 36273,
 "impressions": 56746,
 "installs": None,
 "views": 86867,
 "campaign_id": "287634828273"
},
{
 "start_time": "2020-01-23T15:26:17+0900",
 "end_time": "2020-01-23T15:26:17+0900",
 "reach": 37846,
 "spend": 21726,
 "clicks": 6237,
 "impressions": 45748,
 "installs": 1293,
 "views": 23643,
 "campaign_id": "287634828272"
},
{
 "start_time": "2020-01-23T15:26:17+0900",
 "end_time": "2020-01-23T15:26:17+0900",
 "reach": None,
 "spend": 263452,
 "clicks": "73812",
 "impressions": 2382,
 "installs": 213,
 "campaign_id": "287634828273"
},
{
 "start_time": "2020-01-24T15:26:17+0900",
 "end_time": "2020-01-24T15:26:17+0900",
 "reach": 67867,
 "spend": "27362",
 "clicks": "81723",
 "impressions": 61237,
 "views": 36872,
 "campaign_id": "287634828272"
},
]}

print(json.dumps(sample_data, ensure_ascii= False, indent="\t"))

with open('data.json', 'w', encoding="utf-8") as make_file:
    json.dump(sample_data, make_file, ensure_ascii=False, indent="\t")