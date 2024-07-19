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
        print(r.content)
        f.write(r.content)
        return f
    
retrieve_video("https://v16-webapp-prime.tiktok.com/video/tos/maliva/tos-maliva-ve-0068c799-us/og2Qcov7EIEDHvDh34ZiBKBUWuiPgnoJiCMAv/?a=1988&bti=NDU3ZjAwOg%3D%3D&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=6128&bt=3064&cs=0&ds=6&ft=4fUEKMMD8Zmo0WZa3-4jV1te8pWrKsd.&mime_type=video_mp4&qs=0&rc=OTc2Mzk3ZTg0N2Q3Z2Y3ZkBpajpnbXU5cjU1dDMzZzczNEAwMi9eNS9iXi0xMDUwMl4uYSNkbGxvMmRrczJgLS1kMS9zcw%3D%3D&btag=e00090000&expire=1721515768&l=2024071822474342565774FF583606E1A4&ply_type=2&policy=2&signature=18c280025df0798c3d08347dbc5e6549&tk=tt_chain_token")