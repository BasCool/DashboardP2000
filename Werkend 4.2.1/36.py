from eca import *
import random
from eca.generators import start_offline_tweets
import eca.http
import datetime
import textwrap
from util import *

## You might have to update the root path to point to the correct path
## (by default, it points to <rules>_static)
root_content_path = '36_static'

def add_request_handlers(httpd):
    httpd.add_route('/api/order', eca.http.GenerateEvent('order'), methods=['POST'])
    httpd.add_route('/api/filter', eca.http.GenerateEvent('filterevent'), methods=['POST'])
    httpd.add_content('/lib/', '36_static/lib')
    httpd.add_content('/style/', '36_static/style')
 
@event('init')
def setup(ctx, e):
	#tweets = getTweetsArray()
	hoi = 1
	#start_offline_tweets('p2000.txt', time_factor=200, event_name='start1')
	#start_offline_tweets('p2000.txt', time_factor=50, event_name='start2')

#@event('start1')
def unfiltfunc(ctx, e):
	tweet = e.data
	#print(tweet)
	emit('unfil', tweet)

#@event('start2')
def filtfunc(ctx, e):
	tweet = e.data
	emit('fil', tweet)

@event('order')
def order(c, e):
	print("Received a new order:")
	print(e.data)
	emit('orders',{
        'text': str(e.data)
    });
	
@event('filterevent')
def filterfunc(c, e):
	#print("Received a new filter:")
	print(e.data)
	emit('filterdisp', {'action': 'reset'})
	emit('filterdisp',{
        'text': str(e.data)
    });