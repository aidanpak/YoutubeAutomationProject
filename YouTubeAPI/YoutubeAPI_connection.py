from googleapiclient.discovery import build

steps:
    - name:api_key
      run:
        echo $API
      env:
        API: ${{ secrets.API_KEY_SECRET }}


class APIConnection:
    Youtube = build('youtube', 'v3', developerKey=api_key)
    #Youtube.close()




