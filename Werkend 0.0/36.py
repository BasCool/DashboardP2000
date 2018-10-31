from eca import *
import random
from eca.generators import start_offline_tweets
import datetime
import textwrap
## You might have to update the root path to point to the correct path
## (by default, it points to <rules>_static)
root_content_path = '36_static'


# binds the 'setup' function as the action for the 'init' event
# the action will be called with the context and the event
@event('init')
def setup(ctx, e):

    start_offline_tweets('p2000.txt', time_factor=200, event_name='start1')
    start_offline_tweets('p2000.txt', time_factor=50, event_name='start2')

@event('start1')
def unfiltered(ctx, e):
    tweet = e.data
    emit('unfiltered', tweet)

@event('start2')
def filtered(ctx, e):
    tweet = e.data
    emit('filtered', tweet)