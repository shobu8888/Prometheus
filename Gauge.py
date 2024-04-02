import http.server
import random
import time
from prometheus_client import start_http_server, Gauge

APP_PORT = 8000
METRICS_PORT = 8001
REQUEST_COUNT = Gauge("app_current_req_metrices", "application current req count" ) 
REQ_SERVE_TIME = Gauge("app_req_serve_metrices", "application req serve count")
RAND_NUM = random.random()*10

class HandleRequests(http.server.BaseHTTPRequestHandler):
    
    @REQUEST_COUNT.track_inprogress()
    def do_GET(self):
        
        #REQUEST_COUNT.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        REQ_SERVE_TIME.set_to_current_time()
        #REQ_SERVE_TIME.set(time.time())
        #REQUEST_COUNT.dec()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()


