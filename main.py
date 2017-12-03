#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        title = "Overtune"
        template_var = {"TITLE": title, "INSTRUMENTS": "class=\"selected\""}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_var))


class TunerHandler(webapp2.RequestHandler):

    def get(self):
        title = "Tuning Box"
        template_var = {"TITLE": title, "TUNER": "class=\"selected\""}
        template = JINJA_ENVIRONMENT.get_template('tuningbox.html')
        self.response.out.write(template.render(template_var))


class MetroHandler(webapp2.RequestHandler):

    def get(self):
        title = "Metronome"
        template_var = {"TITLE": title, "METRO": "class=\"selected\""}
        template = JINJA_ENVIRONMENT.get_template('metronome.html')
        self.response.out.write(template.render(template_var))


class InstrumentHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(self.request.path)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/tuner', TunerHandler),
    ('/metro', MetroHandler),
    ('/instruments/.*', InstrumentHandler)
], debug=True)
