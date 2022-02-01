#!/usr/bin/env python3

"""
 
  Modified from "Modern Python Standard Library Cookbook" by Alessandro Molina
  Web Development > Serving Static Files
  
  Author: Philip McGuire
  Created: 1/31/2022
  Description:
  
     Program starts a development server hosting the static files in the
     directory supplied as the first argument. This server is meant for simple
     development purposes and is not in anyway meant for a production or even
     test environment. 
 
"""

import os.path
import socketserver
from http.server import SimpleHTTPRequestHandler, HTTPServer

def serve_directory(path, port=8000):
    class ConfiguredHandler(HTTPDirectoryRequestHandler):
        SERVED_DIRECTORY = path
    httpd = ThreadingHTTPServer(("", port), ConfiguredHandler)
    print("serving on port", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


class HTTPDirectoryRequestHandler(SimpleHTTPRequestHandler):
    SERVED_DIRECTORY = '.'

    def translate_path(self, path):
        path = super().translate_path(path)
        relpath = os.path.relpath(path)
        return os.path.join(self.SERVED_DIRECTORY, relpath)

serve_directory('docs/')
