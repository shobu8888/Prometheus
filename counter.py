import http.server
import random
from prometheus_client import start_http_server, Counter

APP_PORT = 8000
METRICS_PORT = 8001
REQUEST_COUNT = Counter("app_req_metrices", "application random count" , ["app_name" , "endpoint"]) 
RANDOM_INC = Counter("app_ramdom_metrices", "application http request count")
RAND_NUM = random.random()*10

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        RANDOM_INC.inc(RAND_NUM)
        REQUEST_COUNT.labels("PROM_APP", self.path).inc()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()


