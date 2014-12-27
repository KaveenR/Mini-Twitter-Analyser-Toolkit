from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json

class StdOutListener(StreamListener):

    database = None
    config = None

    def __init__(self,db,config):
        self.database = db
        self.config = config

    def on_data(self, dat):
        data = json.loads(dat)
        tmp = dict(handle = data["user"]["screen_name"],
            text=data["text"],location=data["created_at"],
            indices=data["entities"])
        self.database["tweets"].insert(tmp)
        print("tweet by "+data["user"]["screen_name"]+" on "+config["project-name"]+" recorded")
        return True

    def on_error(self, status):
        print("network error")

if __name__ == '__main__':
    config = None
    auth = None
    client = None
    try:
        config = json.loads(open("config.json").read())
    except:
        print("Config loading/parsing failed")
        exit()
    try:
        client = MongoClient()
    except:
        print("database connection error")
        exit()

    db = client[config["project-name"]]

    l = StdOutListener(db,config)

    try:
        auth = OAuthHandler(config["auth"]["consumer_key"], config["auth"]["consumer_secret"])
    except:
        print("Auth Failed")
        exit()
    
    auth.set_access_token(config["auth"]["access_token"], config["auth"]["access_token_secret"])

    stream = Stream(auth, l)
    stream.filter(track=config["listners"])