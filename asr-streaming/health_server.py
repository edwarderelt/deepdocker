#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "healthy", "service": "moshi-server"}
            self.wfile.write(json.dumps(response).encode())
            logger.info("Health check requested - returned 200 OK")
        else:
            self.send_response(404)
            self.end_headers()
            logger.info(f"404 - Path not found: {self.path}")
    
    def log_message(self, format, *args):
        # Override to prevent duplicate logging
        pass

if __name__ == '__main__':
    port = 8081
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, HealthHandler)
    logger.info(f"Health check server starting on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Health check server shutting down")
        httpd.shutdown()