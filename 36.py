from eca import *
import random
from eca.generators import start_offline_tweets
import datetime
import textwrap
import pprint
import re
## You might have to update the root path to point to the correct path
## (by default, it points to <rules>_static)
root_content_path = '36_static'


# binds the 'setup' function as the action for the 'init' event
# the action will be called with the context and the event
@event('init')
def setup(ctx, e):
    start_offline_tweets('p2000.txt', time_factor=150, event_name='chirp')
    #start wordcloud
    ctx.words = {}

pattern = re.compile('\W+')

stopwords = ['het', 'een', 'aan', 'zijn', 'http', 'www', 'com', 'ben', 'jij']

def words(message):
    result = pattern.split(message)
    result = map(lambda w: w.lower(), result)
    result = filter(lambda w: w not in stopwords, result)
    result = filter(lambda w: len(w) > 2, result)
    return result
#end wordcloud

@event('chirp')
def tweet(ctx, e):
    tweet = e.data
    emit('tweet', tweet)
#start wordcloud
    for w in words(tweet['text']):
        emit('wordcloud', {
            'action': 'add',
            'value': (w, 1)
        })
#end wordcloud
