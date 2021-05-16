from googleapiclient.discovery import build
import config_API #secrets_file with your API Key

#accessing your API key from secrets file
api_key = config_API.API_key



class APIConnection:
    Youtube = build('youtube', 'v3', developerKey=api_key)
    #Youtube.close()




