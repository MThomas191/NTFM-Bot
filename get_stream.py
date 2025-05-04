from yt_dlp import YoutubeDL

def get_stream_url(video_url, playlist=False):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': not playlist,
        'quiet': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            if playlist and 'entries' in info:
                return [entry['url'] for entry in info['entries']]
            return info['url']
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test URLs
test_urls = [
    ("https://www.youtube.com/watch?v=mSEUpJIg52U", False),
    ("https://www.youtube.com/playlist?list=AAY0P-fiuyKkC2Eu", True),
]
for url, is_playlist in test_urls:
    stream_url = get_stream_url(url, is_playlist)
    print(f"Input: {url}\nStream: {stream_url}\n")