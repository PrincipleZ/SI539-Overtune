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

template_var = {}

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
guitar_dict = {
    "TITLE": "GUITAR",
    "INSTRUMENT": "GUITAR",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/guitar/notes/1.mp3",
    "AUDIO2": "sounds/guitar/notes/2.mp3",
    "AUDIO3": "sounds/guitar/notes/3.mp3",
    "AUDIO4": "sounds/guitar/notes/4.mp3",
    "AUDIO5": "sounds/guitar/notes/5.mp3",
    "AUDIO6": "sounds/guitar/notes/6.mp3",
    "AUDIO7": "sounds/guitar/notes/7.mp3",
    "AUDIO8": "sounds/guitar/notes/8.mp3",
    "RANGE_LOW": "E2",
    "RANGE_HIGH": "E6",
    "VIDEO0": "https://www.youtube.com/watch?v=qv23U4uNaU8",
    "VIDEO1": "https://www.youtube.com/watch?v=6ny8htqHHuM",
    "VIDEO2": "https://www.youtube.com/watch?v=t5iz41Hk_wI",
    "THUMBNAIL0": "img/thumbnails/guitar_01.png",
    "THUMBNAIL1": "img/thumbnails/guitar_02.png",
    "THUMBNAIL2": "img/thumbnails/guitar_03.png",
    "TITLE0": "Solo Acoustic Guitar",
    "MUSIC0": "sounds/guitar/music/0.mp3",
    "TITLE1": "A Garden and A Library",
    "MUSIC1": "sounds/guitar/music/1.mp3",
    "TITLE2": "A Stranger's Map of Texas",
    "MUSIC2": "sounds/guitar/music/2.mp3",
    "TAG1_STYLE": "left:42px;",
    "TAG2_STYLE": "left:174px;",
    "RANGE_STYLE": "margin-left: 20%;",
    "INSTRUMENT_PIC": "img/guitar1.png",
    "INTRODUCTION": "The guitar is a fretted musical instrument that usually has six strings. The sound is projected either acoustically, using a hollow wooden or plastic and wood box, or through electrical amplifier and a speaker."}
harp_dict = {}
trumpet_dict = {}
piano_dict = {
    "TITLE": "PIANO",
    "INSTRUMENT": "PIANO",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/piano/notes/1.mp3",
    "AUDIO2": "sounds/piano/notes/2.mp3",
    "AUDIO3": "sounds/piano/notes/3.mp3",
    "AUDIO4": "sounds/piano/notes/4.mp3",
    "AUDIO5": "sounds/piano/notes/5.mp3",
    "AUDIO6": "sounds/piano/notes/6.mp3",
    "AUDIO7": "sounds/piano/notes/7.mp3",
    "AUDIO8": "sounds/piano/notes/8.mp3",
    "RANGE_LOW": "A0",
    "RANGE_HIGH": "B7",
    "VIDEO0": "https://www.youtube.com/watch?v=oAXXSFKfjLs",
    "VIDEO1": "https://www.youtube.com/watch?v=7maJOI3QMu0",
    "VIDEO2": "https://www.youtube.com/watch?v=0V_-DQdUvGQ",
    "THUMBNAIL0": "img/thumbnails/piano_01.png",
    "THUMBNAIL1": "img/thumbnails/piano_02.png",
    "THUMBNAIL2": "img/thumbnails/piano_03.png",
    "TITLE0": "To Elise",
    "MUSIC0": "sounds/piano/music/0.mp3",
    "TITLE1": "Chopin nocturnes Op.9 No.2",
    "MUSIC1": "sounds/piano/music/1.mp3",
    "TITLE2": "Bach - Prelude and Fugue in C",
    "MUSIC2": "sounds/piano/music/2.mp3",
    "TAG1_STYLE": "left:-18px;",
    "TAG2_STYLE": "left:234px;",
    "RANGE_STYLE": "width: 100%;margin-left: 0;",
    "INSTRUMENT_PIC": "img/piano1.png",
    "INTRODUCTION": "The piano is an acoustic, stringed musical instrument invented in Italy by Bartolomeo Cristofori around the year 1700, in which the strings are struck by hammers."}
eguitar_dict = {
    "TITLE": "EGUITAR",
    "INSTRUMENT": "ELECTRONIC<br>GUITAR",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/electric_guitar/notes/1.mp3",
    "AUDIO2": "sounds/electric_guitar/notes/2.mp3",
    "AUDIO3": "sounds/electric_guitar/notes/3.mp3",
    "AUDIO4": "sounds/electric_guitar/notes/4.mp3",
    "AUDIO5": "sounds/electric_guitar/notes/5.mp3",
    "AUDIO6": "sounds/electric_guitar/notes/6.mp3",
    "AUDIO7": "sounds/electric_guitar/notes/7.mp3",
    "AUDIO8": "sounds/electric_guitar/notes/8.mp3",
    "RANGE_LOW": "E2",
    "RANGE_HIGH": "E6",
    "VIDEO0": "https://www.youtube.com/watch?v=l_NoccF3RaI",
    "VIDEO1": "https://www.youtube.com/watch?v=4iV2LsHRDJE",
    "VIDEO2": "https://www.youtube.com/watch?v=Yjarkl3VWPE",
    "THUMBNAIL0": "img/thumbnails/eguitar_01.png",
    "THUMBNAIL1": "img/thumbnails/eguitar_02.png",
    "THUMBNAIL2": "img/thumbnails/eguitar_03.png",
    "TITLE0": "Hotel California",
    "MUSIC0": "sounds/electric_guitar/music/0.mp3",
    "TITLE1": "Anagnorisis",
    "MUSIC1": "sounds/electric_guitar/music/1.mp3",
    "TITLE2": "Linger",
    "MUSIC2": "sounds/electric_guitar/music/2.mp3",
    "TAG1_STYLE": "left:42px;",
    "TAG2_STYLE": "left:174px;",
    "RANGE_STYLE": "margin-left: 20%;",
    "INSTRUMENT_PIC": "img/electronicguitar1.png",
    "INTRODUCTION": "An electric guitar is a fretted stringed instrument with a neck and body that uses a pickup to convert the vibration of its strings into electrical signals. The vibration occurs when a guitarist strums, plucks, fingerpicks, or taps the strings."}
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
        if instrument_name in instruments_dict:
            template_var = instruments_dict[instrument_name]
        template = JINJA_ENVIRONMENT.get_template('instrumenttemplate.html')
        try:
            self.response.out.write(template.render(template_var))
        except:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/tuner', TunerHandler),
    ('/metro', MetroHandler),
    ('/.*', InstrumentHandler)
], debug=True)
