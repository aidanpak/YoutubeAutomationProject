from YoutubeAPI_connection import APIConnection



def get_subscriber_list():
    request = APIConnection.Youtube.subscriptions().list(
        part = 'snippet',
        channelId = 'UC1v5V2rZ061NYDqwbHFt83A',
    )
    list = request.execute()
    for parameter in list:
        print(parameter)

    return list
    [snippet]


print(get_subscriber_list())

def subscriber_list_usernames(list):
    pass
