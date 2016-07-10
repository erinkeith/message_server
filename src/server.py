#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import events
import processor
import sites


STATS_FILE = 'stats.json'
EVENTS_ENDPOINT = '/events'
our_sites = sites.Sites()
messages = []


class MessageHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        if self.path == EVENTS_ENDPOINT:
            post_form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })

            if post_form:
                new_event = events.PostEvent(post_form)
                processor.process_event(new_event, our_sites, messages)

    def do_GET(self):
        self._set_headers()
        if self.path == '/' + STATS_FILE:
            with open(STATS_FILE, 'r') as stats_file:
                self.wfile.write(stats_file.read())

if __name__ == '__main__':
    server = HTTPServer(("", 80), MessageHandler)
    print 'Starting MessageServer, use <Ctrl-C> to stop'
    server.serve_forever()
