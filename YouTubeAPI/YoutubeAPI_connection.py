from googleapiclient.discovery import build

api_key = 'AIzaSyBw1R3xD_LlKNZ8DMQTzIzFklq-ZA1CT_U'

class APIConnection:
    Youtube = build('youtube', 'v3', developerKey=api_key)
    #Youtube.close()




