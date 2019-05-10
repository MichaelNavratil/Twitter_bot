
#This app uses the tweepy libary 
import tweepy 

#This Section is where the user will put the tokens used for authentication must fill in with your tokens 
consumer_key = '' 
consumer_secret = ''
access_token = '' 
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
 

api.update_status('') #This 
