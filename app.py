from chalice import Chalice
import youtube_dl


app = Chalice(app_name='youtube_api')

dl = youtube_dl.YoutubeDL()


@app.route('/')
def index():
    request = app.current_request
    query_params = request.query_params
    
    url = query_params.get('url') if query_params else ''
    if url:
        code = 0
        data = dl.extract_info(url, download=False)
    else:
        code = 1
        data = {}

    return {
        'code': code,
        'data': data,
    }
