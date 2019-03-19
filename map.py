import json
import pandas as pd
import os
tweets_data_path = 'twitter_data.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


def populate_tweet_df(tweets_data):
    df = pd.DataFrame()

    df['text'] = list(map(lambda tweet: tweet['text'],tweets_data))

    df['location'] = list(map(lambda tweet: tweet['user']['location'], tweets_data))

    df['country_code'] = list(map(lambda tweet: tweet['place']['country_code']
    if tweet['place'] != None else '', tweets_data))

    df['long'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][0]
    if tweet['coordinates'] != None else 'NaN', tweets_data))

    df['latt'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][1]
    if tweet['coordinates'] != None else 'NaN', tweets_data))

    df['filter_tweet']=df['latt'].value_counts()
    df['sentiment_tweet']=list(map(lambda tweet: tweet['text']
    if tweet['coordinates'] != None else 'NaN', tweets_data))

    return df
df = populate_tweet_df(tweets_data)
#print(df['filter_tweet']
longs=[]
latts=[]
l1=[]
for (m,n,o) in zip(df['long'],df['latt'],df['text']):
    if m=='NaN' or n=='NaN':
        pass
    else:
        longs.append(m)
        latts.append(n)
        l1.append(o)
#print(l1)
print(len(l1))
print(len(df['text']))
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.figure(figsize=(30,12))

# plot the blank world map/foilum
#ortho,merc,aquad
my_map = Basemap(projection='merc', lat_0=50, lon_0=-100,
                 resolution='l', area_thresh=5000.0,
                 llcrnrlon=-140, llcrnrlat=-55,
                 urcrnrlon=160, urcrnrlat=70)
# set resolution='h' for high quality
# my_map.drawmapboundary(fill_color='aqua')
# my_map.fillcontinents(color='coral',lake_color='aqua')

# draw elements onto the world map
my_map.drawcountries()

my_map.drawstates()
my_map.drawcoastlines(antialiased=False,
                      linewidth=0.005)

# add coordinates as red dots
#longs = list(df.loc[(df.long != 'NaN')].long)
#print(longs)

#latts = list(df.loc[df.latt != 'NaN'].latt)
x, y = my_map(longs, latts)
import time
from paralleldots import set_api_key, get_api_key, sentiment
set_api_key("6dm9k0RomplpimtZETEkwp6JzMTrPSDhhMIiGPGmu68")
get_api_key()
for (t,u,v) in zip(l1,x,y):
    a = sentiment(t)
    time.sleep(4)
    print(a)
    if a['sentiment'] == 'positive':
        my_map.plot(u, v,'ro',marker='D',color='r', markersize=9, alpha=0.8)
    elif a['sentiment'] == 'negative':
        my_map.plot(u, v,'ro',marker='D',color='b', markersize=9, alpha=0.8)
    elif a['sentiment'] == 'neutral':
        my_map.plot(u, v,'ro',marker='D',color='m', markersize=9, alpha=0.8)
country_latts=[33.93911,47.516231,-25.274398,23.684994,17.189877,56.130366,35.86166,55.378051,20.593684,36.204824,-0.023559,37.09024,-11.202692,-3.373056,41.153332]
country_longs=[67.709953,14.550072,133.775136,90.356331,-88.49765,-106.346771	,104.195397,-3.435973,78.96288,138.252924,37.906193,-95.712891,17.873887,29.918886,20.168331	]
country_name=['Afghanistan','Austria','Australia','Bangladesh','Belize','Canada','China','United Kingdom','India','Japan','Kenya','United States','Angola','Burundi','Albania']
x, y = my_map(country_longs, country_latts)
for a,b,z in zip(x,y,country_name):
    plt.text(a,b,z,fontsize=12,fontweight='bold',ha='left',va='center',color='b')



plt.show()