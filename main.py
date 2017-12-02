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
        template_var = {"TITLE": title, "HOME": "class=\"selected\""}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_var))


class ProjectHandler(webapp2.RequestHandler):

    def get(self):
        title = "Projects"
        template_var = {"TITLE": title, "PROJECTS": "class=\"current\""}
        template = JINJA_ENVIRONMENT.get_template('projects.html')
        self.response.out.write(template.render(template_var))


class RandomHandler(webapp2.RequestHandler):

    def get(self):
        title = "Random Things"
        template_var = {"TITLE": title, "RANDOMS": "class=\"current\""}
        template = JINJA_ENVIRONMENT.get_template('randoms.html')
        self.response.out.write(template.render(template_var))


class ContactHandler(webapp2.RequestHandler):

    def get(self):
        title = "Contact me"
        template_var = {"TITLE": title, "CONTACT": "class=\"current\""}
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.out.write(template.render(template_var))


class EventifyHandler(webapp2.RequestHandler):

    def get(self):
        title = "Eventify"
        template_var = {"TITLE": title, "PROJECTS": "class=\"current\""}
        template = JINJA_ENVIRONMENT.get_template('eventify.html')
        self.response.out.write(template.render(template_var))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/projects', ProjectHandler),
    ('/randoms', RandomHandler),
    ('/contact', ContactHandler),
    ('/eventify', EventifyHandler)
], debug=True)
