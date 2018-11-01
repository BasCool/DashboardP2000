from eca import *
import random
from eca.generators import start_offline_tweets
import eca.http
import datetime
import textwrap
import json

filtersett2 = 1
print("hatsikidee")
root_content_path = '36_static'

def add_request_handlers(httpd):
    httpd.add_route('/api/order', eca.http.GenerateEvent('order'), methods=['POST'])
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
    try:
        print("sett " + str(filtersett2))
        if filter(tweet):
            emit('fil', tweet)
            print(len(tweet))
    except:
        emit('fil', tweet)

@event('start2')
def unfiltfunc(ctx, e):
    tweet = e.data
    emit('unfil', tweet)

def filter(tweet):
    if len(tweet) >= filtersett2:
        return True
    else:
        return False
    
@event('filterevent')
def filterfunc(c, e):
    filtersett2 = 24
    print("nu issie: " + str(filtersett2))
    filterset = e.data
    print(filterset)
    print(filterset['police'][0])
    #emit('filterdisp',{
    #    'text': str(x)
    #});
