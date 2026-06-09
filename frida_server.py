"""
FRIDA — Local dev server with Copernicus CORS proxy
====================================================
Replaces `python -m http.server 8000`.

This server does TWO things:
1. Serves static files (your HTML, etc.) — same as http.server
2. Proxies /proxy/copernicus/* requests to Copernicus API,
   bypassing the CORS restriction that blocks direct browser access.

USAGE:
  cd C:\\Users\\USER\\Documents\\frida-app
  python frida_server.py

Then open: http://localhost:8000/index_v44.html?test=1

PROXY ENDPOINTS:
  /proxy/copernicus/token   → POST to identity.dataspace.copernicus.eu OAuth
  /proxy/copernicus/catalog → POST to sh.dataspace.copernicus.eu/api/v1/catalog/...
  /proxy/copernicus/process → POST to sh.dataspace.copernicus.eu/api/v1/process

The proxy only forwards to copernicus.eu domains, never anywhere else.
"""

import http.server
import socketserver
import urllib.request
import urllib.error
import json
import sys

PORT = 8000

# Allowed upstream hosts (security: prevent open proxy abuse)
ALLOWED_UPSTREAM = {
    '/proxy/copernicus/token':   'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token',
    '/proxy/copernicus/catalog': 'https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search',
    '/proxy/copernicus/process': 'https://sh.dataspace.copernicus.eu/api/v1/process',
}


class FridaHandler(http.server.SimpleHTTPRequestHandler):
    
    def _add_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Access-Control-Max-Age', '86400')
    
    def do_OPTIONS(self):
        # Preflight CORS request
        self.send_response(204)
        self._add_cors_headers()
        self.end_headers()
    
    def do_POST(self):
        # Only POSTs to /proxy/copernicus/* are allowed
        path = self.path.split('?')[0]
        if path not in ALLOWED_UPSTREAM:
            self.send_response(404)
            self._add_cors_headers()
            self.end_headers()
            self.wfile.write(b'Proxy endpoint not allowed')
            return
        
        upstream = ALLOWED_UPSTREAM[path]
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else b''
        
        # Build upstream request
        upstream_headers = {}
        # Forward content-type and authorization
        for h in ('Content-Type', 'Authorization'):
            v = self.headers.get(h)
            if v:
                upstream_headers[h] = v
        
        req = urllib.request.Request(upstream, data=body, headers=upstream_headers, method='POST')
        
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                response_body = resp.read()
                status = resp.status
                content_type = resp.headers.get('Content-Type', 'application/json')
                
                self.send_response(status)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Length', str(len(response_body)))
                self._add_cors_headers()
                self.end_headers()
                self.wfile.write(response_body)
                print(f"[PROXY] {path} -> {status} ({len(response_body)} bytes)")
        except urllib.error.HTTPError as e:
            error_body = e.read()
            self.send_response(e.code)
            self.send_header('Content-Type', 'application/json')
            self._add_cors_headers()
            self.end_headers()
            self.wfile.write(error_body)
            print(f"[PROXY] {path} -> HTTP {e.code}: {error_body[:100]}")
        except Exception as e:
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self._add_cors_headers()
            self.end_headers()
            err = json.dumps({'proxy_error': str(e)}).encode()
            self.wfile.write(err)
            print(f"[PROXY ERROR] {path} -> {e}")
    
    def end_headers(self):
        # Add CORS to all GET responses too (for static files)
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Cleaner log output
        sys.stdout.write(f"  {self.address_string()} - {format % args}\n")


if __name__ == '__main__':
    with socketserver.ThreadingTCPServer(("", PORT), FridaHandler) as httpd:
        print(f"FRIDA dev server running on http://localhost:{PORT}")
        print(f"  - Serves static files from current directory")
        print(f"  - Proxies Copernicus API to bypass CORS")
        print(f"  - Open: http://localhost:{PORT}/index_v44.html?test=1")
        print(f"  - Press Ctrl+C to stop")
        print()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down.")
