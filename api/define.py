from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    # dic = dict(query_string_list)
    
    url = "https://restcountries.com/v3.1/name"
    full_url = url +dic["word"]
    response = requests.get(full_url)
    data = response.json()
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "{url}"
    self.wfile.write(str(message).encode())
    return
  
    #   definitions = []
    # for word_data in data:
    #   definition = word_data["meanings"][0]