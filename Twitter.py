import tweepy
import sys
while True:
    print("1.Retrive tweets")
    print("2.Count the followers")
    print("3.Determine the status")
    print("4.Location language and Time Zone")
    print("5.compare tweets")
    print("6.Analyse the top usage")
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
    def retrive():
        m=str(input("enter any HASH tag for search:"))
        tweets=api.search(m,lang='en',count="10",tweet_mode='extended')
        print("tweets")
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
        loc=input("enter any location: ")
        api.update_status(status,user_id,loc,loc)
    if choice==1:
        retrive()
    if choice==2:
        followers()
    if choice==3:
        status()
    if choice==8:
        exit()


