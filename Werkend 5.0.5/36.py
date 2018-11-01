from eca import *
import random
from eca.generators import start_offline_tweets
import eca.http
import datetime
import textwrap
import json
from tweetUtil import *

filterset = {'adam': ['on'], 'rdam': ['on'], 'zwol': ['on'], 'lwar': ['on'], 'nhln': ['on'], 'tilb': ['on'], 'gtrb': ['on'], 'harw': ['on'], 'oldb': ['on'], 'oned': ['on'], 'police': ['on'], 'ambu': ['on'], 'firebrig': ['on'], 'prio1': ['on'], 'prio2': ['on'], 'prio3': ['on'], 'time-start': '', 'time-end': '', 'date-start': '', 'date-end': ''}

filtertweet = {'created_at': '', 'id': 380425314650042368, 'id_str': '380425314650042368', 'text': '<h3>NEW FILTER ACTIVE!!<h3>', 'source': '<a href="" rel="nofollow">watiserloos.in</a>', 'truncated': False, 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 291158798, 'id_str': '291158798', 'name': 'System', 'screen_name': 'BasBankje', 'location': '', 'url': None, 'description': None, 'protected': False, 'followers_count': 4, 'friends_count': 6, 'listed_count': 0, 'created_at': 'Sun May 01 15:10:05 +0000 2011', 'favourites_count': 0, 'utc_offset': 7200, 'time_zone': 'Amsterdam', 'geo_enabled': True, 'verified': False, 'statuses_count': 9841, 'lang': 'nl', 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_0_normal.png', 'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_0_normal.png', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'default_profile': True, 'default_profile_image': True, 'following': None, 'follow_request_sent': None, 'notifications': None}, 'geo': {'type': 'Point', 'coordinates': [52.3587642, 4.8056984]}, 'coordinates': {'type': 'Point', 'coordinates': [4.8056984, 52.3587642]}, 'place': {'id': '99cdab25eddd6bce', 'url': 'https://api.twitter.com/1.1/geo/id/99cdab25eddd6bce.json', 'place_type': 'city', 'name': 'Amsterdam', 'full_name': 'Amsterdam, Noord-Holland', 'country_code': 'NL', 'country': 'Nederland', 'bounding_box': {'type': 'Polygon', 'coordinates': [[[4.7288999, 52.278226599999996], [4.7288999, 52.4312289], [5.0792072, 52.4312289], [5.0792072, 52.278226599999996]]]}, 'attributes': {}}, 'contributors': None, 'retweet_count': 0, 'favorite_count': 0, 'entities': {'hashtags': [], 'symbols': [], 'urls': [{'url': '', 'expanded_url': '', 'display_url': '', 'indices': [35, 57]}], 'user_mentions': []}, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'filter_level': 'medium', 'lang': 'nl'}

root_content_path = '36_static'

def add_request_handlers(httpd):
    httpd.add_route('/api/filter', eca.http.GenerateEvent('filterevent'), methods=['POST'])
    httpd.add_content('/lib/', '36_static/lib')
    httpd.add_content('/style/', '36_static/style')
 
@event('init')
def setup(ctx, e):
    #tweets = getTweetsArray()
    start_offline_tweets('p2000.txt', time_factor=75, event_name='start1')
    start_offline_tweets('p2000.txt', time_factor=75, event_name='start2')

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
    emit('fil', filtertweet)
    #print(filterset['police'][0])
    #emit('filterdisp',{
    #    'text': str(x)
    #});