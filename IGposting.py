import requests
import json
from config import user_id, user_key, video_link

def create_container(): 
    caption = "beta testing..."
    container_request = requests.post(url = f"https://graph.instagram.com/v20.0/{user_id}/media",
                      params={
                          "media_type" : "REELS",
                          "video_url" : video_link,
                          "caption" : caption, 
                          "share_to_feed": True,
                          "access_token": user_key
                      })
    print(container_request.status_code)
    print(container_request.content)

    #container successfully created
    if(container_request.status_code == 200): 
        containerID = json.loads(container_request.content.decode('utf-8'))["id"]

        print(containerID)
        #check status of container upload
        r = requests.get(url=f"https://graph.instagram.com/{containerID}?fields=status_code",
                         params={
                                 "access_token": user_key})
        
        print(r.status_code)
        print(r.content)

    return
