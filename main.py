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


violin_dict = {
    "TITLE": "VIOLIN",
    "INSTRUMENT": "VIOLIN",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/violin/notes/1.mp3",
    "AUDIO2": "sounds/violin/notes/2.mp3",
    "AUDIO3": "sounds/violin/notes/3.mp3",
    "AUDIO4": "sounds/violin/notes/4.mp3",
    "AUDIO5": "sounds/violin/notes/5.mp3",
    "AUDIO6": "sounds/violin/notes/6.mp3",
    "AUDIO7": "sounds/violin/notes/7.mp3",
    "AUDIO8": "sounds/violin/notes/8.mp3",
    "RANGE_LOW": "G3",
    "RANGE_HIGH": "A7",
    "VIDEO0": "https://www.youtube.com/watch?v=zgaQFLUdUL0&list=RDP2Xdb1ljd3g&index=2",
    "VIDEO1": "https://www.youtube.com/watch?v=bZ_BoOlAXyk",
    "VIDEO2": "https://www.youtube.com/watch?v=mF3DCa4TbD0",
    "THUMBNAIL0": "img/thumbnails/violin_01.jpg",
    "THUMBNAIL1": "img/thumbnails/violin_02.jpg",
    "THUMBNAIL2": "img/thumbnails/violin_03.jpg",
    "TITLE0": "Saint Saens - Introduction and Rondo Capriccioso",
    "MUSIC0": "sounds/violin/music/Introduction_and_Rondo_Capriccioso.mp3",
    "TITLE1": "Secret Garden - Song from a Secret Garden",
    "MUSIC1": "sounds/violin/music/Song_from_a_Secret_Garden.mp3",
    "TITLE2": "Thomas Newman - Por Una Cabeza",
    "MUSIC2": "sounds/violin/music/Por_Una_Cabeza.mp3",
    "TAG1_STYLE": "",
    "TAG2_STYLE": "",
    "RANGE_STYLE": "",
    "INSTRUMENT_PIC": "img/violin1.png",
    "INTRODUCTION": "A wooden string instrument in the violin family: the smallest and highest-pitched instrument."
}
guitar_dict = {}
harp_dict = {}
trumpet_dict = {}
piano_dict = {}
eguitar_dict = {}
accordion_dict = {}
sax_dict = {}

instruments_dict = {
    "violin": violin_dict,
    "guitar": guitar_dict,
    "harp": harp_dict,
    "trumpet": trumpet_dict,
    "piano": piano_dict,
    "eguitar": eguitar_dict,
    "accordion": accordion_dict,
    "sax": sax_dict
}


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
        instrument_name = self.request.path[1:]
        print instrument_name

        template_var = violin_dict
        template = JINJA_ENVIRONMENT.get_template('instrumenttemplate.html')
        self.response.out.write(template.render(template_var))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/tuner', TunerHandler),
    ('/metro', MetroHandler),
    ('/.*', InstrumentHandler)
], debug=True)
