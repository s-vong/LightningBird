import twitter_cred
import twitter

def run():
    api = twitter.Api(twitter_cred.CONSUMER_KEY, 
        twitter_cred.CONSUMER_SECRET, 
        twitter_cred.ACCESS_TOKEN, 
        twitter_cred.ACCESS_SECRET)

    tag_lists = ['sdcc', 'San Diego']
    response = api.GetStreamFilter(track = tag_lists)
    return response
