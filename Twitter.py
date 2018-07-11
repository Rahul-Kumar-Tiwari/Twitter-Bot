import tweepy
from pprint import pprint
import sys
import time
while True:
    print("1.Retrive tweets")
    print("2.Count the followers")
    print("3.Determine the status")
    print("4.Location language and Time Zone")
    print("5.compare tweets")
    print("6.Sentiment the Tweets")
    print("7.Text a message")
    print("8.Exit")
    choice=int(input("Enter your choice: "))
    consumer_key = "uhHcvdFqHeHsRsUUwkXqJgx2L"
    consumer_secret = 'f6q2F7IB4WiEwZj9Bt7Uvtd8QlXOrhRBLCeEAthUrM30UxhqR5'
    access_token = '2492560340-yJLTXsJ2NQuKar73n0FgwBWobGS1ERehqNZsck2'
    access_token_secret = 'Bo3ZglMKQWUGclAID6Yi5vKpdXcXC5URLAoZ6OjGMfgNC'
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    print(api)
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
            print(a)
            if a['sentiment'] == 'positive':
                var1 += 1
            if a['sentiment'] == 'negative':
                var2 += 1
            if a['sentiment'] == 'neutral':
                var3 += 1
        if (var1 > var2) and (var1 > var3):
            print("positive")
        if (var2 > var3) and (var2 > var1):
            print("negative")
        if (var3 > var2) and (var3 > var1):
            print("neutral")
    def comp():
        user_id = input("enter 1st id to Compare:")
        user = api.get_user(user_id)
        a1= user.followers_count
        user_id1 = input("enter 2nd id to Compare:")
        user1 = api.get_user(user_id1)
        a2 = user1.followers_count
        if a1>a2:
            print("{} is the best user of twitter".format(user.name))
        else:
            print("{} is the best user of twitter".format(user1.name))

    if choice==1:om0m
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
    if choice==8:
        exit()


