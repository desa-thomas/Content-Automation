import requests

"""
    Retrieves video from URL
    parameters: 
        url - URL of video to retrieve
    returns: 
        f   - mp4 file of video
"""
def retrieve_video(url): 
    #file name to save video to
    filename = "video.mp4"
    #headers so tiktok doesn't give me a 403
    headers = {'user-agent': 'Mozilla/5.0'}

    r = requests.get(url, headers=headers)
    with open(filename,'wb') as f: 
        f.write(r.content)
        return f

