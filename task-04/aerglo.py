import argparse
import requests 
import webbrowser


parse=argparse.ArgumentParser(description='Enter the date and ID of the required image')
parse.add_argument('date',
                    metavar='date',
                    type=str,
                    help='Date captured')
parse.add_argument('id',
                    metavar='id',
                    type=int,
                    help='Image Id')
args=parse.parse_args()
DATE=args.date
ID=args.id
rover=['curiosity','opportunity','spirit']
l=len(rover)
for a in range(l):
    req=requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/'+rover[a]+'/photos?earth_date='+DATE+'&api_key=DEMO_KEY')
    r=req.json()

    for b in range(len(r['photos'])):
        if (r['photos'][b]['id']==ID):
            webbrowser.open(r['photos'][b]['img_src'])
        