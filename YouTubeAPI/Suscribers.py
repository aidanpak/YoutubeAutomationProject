'''
issue right now is that subscribes maximum is on different page..
'''

from YoutubeAPI_connection import APIConnection




def get_subscriber_list():
    request = APIConnection.Youtube.subscriptions().list(
        part="snippet",
        channelId="UC1v5V2rZ061NYDqwbHFt83A",
        maxResults = 50
    )
    response = request.execute()
    return response



def unpack_subscribers_dict(text):
    items= text['items']
    length = len(items)
    for sub in items:
        print(sub['snippet']['title'])



def subscriber_list_usernames(list):
    pass

subscribers_dict = get_subscriber_list()
print(unpack_subscribers_dict(subscribers_dict))

