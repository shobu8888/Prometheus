import http.server
import random
import time
from prometheus_client import start_http_server, Summary

APP_PORT = 8000
METRICS_PORT = 8001
REQUEST_LATENCY = Summary("app_Req_Latency_metrices", "application request latency  count" ) 



class HandleRequests(http.server.BaseHTTPRequestHandler):
    
    @REQUEST_LATENCY.time()
    def do_GET(self):
        
        #start_time = time.time()
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        #time_taken = time.time() - start_time
        #REQUEST_LATENCY.observe(time_taken)

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()


