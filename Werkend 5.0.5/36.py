from eca import *
import random
from eca.generators import start_offline_tweets
import eca.http
import datetime
import textwrap
import json
from tweetUtil import *

filterset = {'adam': ['on'], 'rdam': ['on'], 'zwol': ['on'], 'lwar': ['on'], 'nhln': ['on'], 'tilb': ['on'], 'gtrb': ['on'], 'harw': ['on'], 'oldb': ['on'], 'oned': ['on'], 'police': ['on'], 'ambu': ['on'], 'firebrig': ['on'], 'prio1': ['on'], 'prio2': ['on'], 'prio3': ['on'], 'time-start': '', 'time-end': '', 'date-start': '', 'date-end': ''}

root_content_path = '36_static'

def add_request_handlers(httpd):
    httpd.add_route('/api/filter', eca.http.GenerateEvent('filterevent'), methods=['POST'])
    httpd.add_content('/lib/', '36_static/lib')
    httpd.add_content('/style/', '36_static/style')
 
@event('init')
def setup(ctx, e):
    #tweets = getTweetsArray()
    start_offline_tweets('p2000.txt', time_factor=50, event_name='start1')
    start_offline_tweets('p2000.txt', time_factor=50, event_name='start2')

@event('start1')
def filtfunc(ctx, e):
    tweet = e.data
    #print("setting: " + str(filterset))
    if filterTweet(tweet,filterset):
        emit('fil', tweet)
    print(filterTweet(tweet,filterset))
		
@event('start2')
def unfiltfunc(ctx, e):
    tweet = e.data
    emit('unfil', tweet)

    
@event('filterevent')
def filterfunc(c, e):
    global filterset
    filterset = e.data
    print(filterset)
    #print(filterset['police'][0])
    #emit('filterdisp',{
    #    'text': str(x)
    #});