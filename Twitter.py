import tweepy
from tweepy.streaming import  StreamListener
import sys
import re
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
while True:

    print("1.Retrive tweets:")
    print("2.Count the followers:")
    print("3.Update the status:")
    print("4.Get Location,language and Time Zone:")
    print("5.compare the Twitter users:")
    print("6.Sentiment the Tweets and User:")
    print("7.Text a message:")
    # print("8.Plot the Graph:")
    # print("9.map Ploting")
    print("8.Exit")
    choice=int(input("Enter your choice: "))
    consumer_key = "uhHcvdFqHeHsRsUUwkXqJgx2L"
    consumer_secret = 'f6q2F7IB4WiEwZj9Bt7Uvtd8QlXOrhRBLCeEAthUrM30UxhqR5'
    access_token = '2492560340-yJLTXsJ2NQuKar73n0FgwBWobGS1ERehqNZsck2'
    access_token_secret = 'Bo3ZglMKQWUGclAID6Yi5vKpdXcXC5URLAoZ6OjGMfgNC'
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    def retrive():
        m=str(input("enter any HASH tag for search:"))
        tweets=api.search(m,lang='english',count="50",tweet_mode='extended')
        print(tweets)
        for tweet in tweets:
            print("---------------------------------")
            print(tweet.full_text)
            print("---------------------------------")
    def followers():
        user_id=input("enter any id to Count the followers:")
        user=api.get_user(user_id)
        print("user_id : ",user.screen_name)
        print("user_name:",user.name)
        print("user_following : ",user.friends_count)
        print("followers :",user.followers_count)
        return
    def status():
        status=input("enter any Status: ")
        user_id = input("enter any id to upload the status:")
        api.update_status(status,user_id)
    def loc():
        user_id = input("enter any id to see location:")
        user = api.get_user(user_id)
        print("location :",user.location)
        print("Time Zone:",user.time_zone)
        print("language: ",user.lang)
    def direct_msg():
        user_id= input("enter any id to send msg:")
        msg=input("enter any msg:")
        api.send_direct_message(user=user_id,text=msg)


    def get_tweets(username):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=username, count=20)
        tmp = []
        tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
        for j in tweets_for_csv:
            tmp.append(j)
        var1 = 0
        var2 = 0
        var3 = 0

        print(tmp)
        from paralleldots import set_api_key, get_api_key, sentiment
        set_api_key("6dm9k0RomplpimtZETEkwp6JzMTrPSDhhMIiGPGmu68")
        get_api_key()
        for t in tmp:
            a = sentiment(t)
            print(t,"-->",a)
            time.sleep(1)
            if a['sentiment'] == 'positive':
                var1 += 1
            if a['sentiment'] == 'negative':
                var2 += 1
            if a['sentiment'] == 'neutral':
                var3 += 1
        if (var1 > var2) and (var1 > var3):
            print("This user is positive on Twitter")
        if (var2 > var3) and (var2 > var1):
            print("This user is negative on Twitter")
        if (var3 > var2) and (var3 > var1):
            print("This user is neutral on Twitter")
    def comp():
        user_id = input("enter 1st id to Compare:")
        user = api.get_user(user_id)
        a1= user.followers_count
        user_id1 = input("enter 2nd id to Compare:")
        user1 = api.get_user(user_id1)
        a2 = user1.followers_count
        if a1>a2:
            print("{},'{}' is the best user of twitter".format(user.name,user_id))
        else:
            print("{},{} is the best user of twitter".format(user1.name,user_id1))
    def Ploat_graph():
        #This is a basic listener that just prints received tweets to stdout.
        class StdOutListener(StreamListener):

            def on_data(self, data):
                try:
                    print(data)
                    saveFile=open("twitter_justin_data.txt",'a')
                    saveFile.write(data)
                    saveFile.write("\n")
                    saveFile.close()
                    return True
                except BaseException as e:
                    print('failed on data',str(e))
                    time.sleep(5)

            def on_error(self, status):
                print(status)


        l = StdOutListener()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = tweepy.Stream(auth,l)
        stream.filter(track=['Justin Bieber'])

        tweets_data_path = 'twitter_justin_data.txt'
        tweets_data = []
        tweets_file = open(tweets_data_path, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue
            print(len(tweets_data))
        tweets = pd.DataFrame()
        tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
        tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
        tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))
        tweets_by_lang = tweets['lang'].value_counts()

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)

        ax.set_xlabel('Languages', fontsize=15)
        ax.set_ylabel('Number of tweets', fontsize=15)
        ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
        tweets_by_lang[0:5].plot(ax=ax, kind='bar', color='yellow')

        tweets_by_country = tweets['country'].value_counts()
        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Countries', fontsize=15)
        ax.set_ylabel('Number of tweets', fontsize=15)
        ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
        tweets_by_country[0:5].plot(ax=ax, kind='bar', color='blue')
        print(tweets_by_country)
        plt.show()



    if choice==1:
        retrive()
    if choice==2:
        followers()
    if choice==3:
        status()
    if choice==4:
        loc()
    if choice==5:
        comp()
    if choice==6:
        username = input("enter any user id:")
        get_tweets(username)
    if choice==7:
        direct_msg()
    # if choice==8:
    #     Ploat_graph()
    if choice==10:
        exit()


