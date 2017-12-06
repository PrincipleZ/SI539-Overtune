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
    "INTRODUCTION": "A wooden string instrument in the violin family: the smallest and highest-pitched instrument (Wikipedia, 2017)."
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
    "INTRODUCTION": "The guitar is a fretted musical instrument that usually has six strings. The sound is projected either acoustically, using a hollow wooden or plastic and wood box, or through electrical amplifier and a speaker (Wikipedia, 2017)."}
harp_dict = {
    "TITLE": "HARP",
    "INSTRUMENT": "HARP",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/harp/notes/1.mp3",
    "AUDIO2": "sounds/harp/notes/2.mp3",
    "AUDIO3": "sounds/harp/notes/3.mp3",
    "AUDIO4": "sounds/harp/notes/4.mp3",
    "AUDIO5": "sounds/harp/notes/5.mp3",
    "AUDIO6": "sounds/harp/notes/6.mp3",
    "AUDIO7": "sounds/harp/notes/7.mp3",
    "AUDIO8": "sounds/harp/notes/8.mp3",
    "RANGE_LOW": "C2",
    "RANGE_HIGH": "F7",
    "VIDEO0": "https://www.youtube.com/watch?v=P2Xdb1ljd3g",
    "VIDEO1": "https://www.youtube.com/watch?v=WTe6t6eyUQ4",
    "VIDEO2": "https://www.youtube.com/watch?v=TnYCW8eWqQo",
    "THUMBNAIL0": "img/thumbnails/harp_01.jpg",
    "THUMBNAIL1": "img/thumbnails/harp_02.jpg",
    "THUMBNAIL2": "img/thumbnails/harp_03.jpg",
    "TITLE0": "Canon",
    "MUSIC0": "sounds/harp/music/Canon.mp3",
    "TITLE1": "Etude in E major OP.10-3",
    "MUSIC1": "sounds/harp/music/Etude in E major OP.10-3.mp3",
    "TITLE2": "Greensleeves",
    "MUSIC2": "sounds/trumpet/music/Greensleeves.mp3",
    "TAG1_STYLE": "left:34px;",
    "TAG2_STYLE": "left:210px;",
    "RANGE_STYLE": "margin-left: 17%; width:75%",
    "INSTRUMENT_PIC": "img/harp1.png",
    "INTRODUCTION": "The harp is a stringed musical instrument that has a number of individual strings running at an angle to its soundboard; the strings are plucked with the fingers (Wikipedia, 2017)."}
trumpet_dict = {
    "TITLE": "TRUMPET",
    "INSTRUMENT": "TRUMPET",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/trumpet/notes/1.mp3",
    "AUDIO2": "sounds/trumpet/notes/2.mp3",
    "AUDIO3": "sounds/trumpet/notes/3.mp3",
    "AUDIO4": "sounds/trumpet/notes/4.mp3",
    "AUDIO5": "sounds/trumpet/notes/5.mp3",
    "AUDIO6": "sounds/trumpet/notes/6.mp3",
    "AUDIO7": "sounds/trumpet/notes/7.mp3",
    "AUDIO8": "sounds/trumpet/notes/8.mp3",
    "RANGE_LOW": "E3",
    "RANGE_HIGH": "C6",
    "VIDEO0": "https://www.youtube.com/watch?v=QcIp7K2UFgE",
    "VIDEO1": "https://www.youtube.com/watch?v=5VYm2PFJ9iM",
    "VIDEO2": "https://www.youtube.com/watch?v=gUij8FCg0z8",
    "THUMBNAIL0": "img/thumbnails/trumpet_01.jpg",
    "THUMBNAIL1": "img/thumbnails/trumpet_02.jpg",
    "THUMBNAIL2": "img/thumbnails/trumpet_03.jpg",
    "TITLE0": "A Comme Amour-Sylvia Tussaud",
    "MUSIC0": "sounds/trumpet/music/A Comme Amour-Sylvia Tussaud.mp3",
    "TITLE1": "Auld Lang Syne-Shield",
    "MUSIC1": "sounds/trumpet/music/Auld Lang Syne-Shield.mp3",
    "TITLE2": "Jintangjia - Zhixiang Li",
    "MUSIC2": "sounds/trumpet/music/Jintangjia - Zhixiang Li.mp3",
    "TAG1_STYLE": "left:70px;",
    "TAG2_STYLE": "left:174px;",
    "RANGE_STYLE": "margin-left: 30%; width:50%;",
    "INSTRUMENT_PIC": "img/trumpet1.png",
    "INTRODUCTION": "A trumpet is a blown musical instrument commonly used in classical and jazz ensembles (Wikipedia, 2017)."}
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
    "INTRODUCTION": "The piano is an acoustic, stringed musical instrument invented in Italy by Bartolomeo Cristofori around the year 1700, in which the strings are struck by hammers (Wikipedia, 2017)."}
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
    "INTRODUCTION": "An electric guitar is a fretted stringed instrument with a neck and body that uses a pickup to convert the vibration of its strings into electrical signals. The vibration occurs when a guitarist strums, plucks, fingerpicks, or taps the strings (Wikipedia, 2017)."}
accordion_dict = {
    "TITLE": "ACCORDION",
    "INSTRUMENT": "ACCORDION",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/accordion/notes/1.mp3",
    "AUDIO2": "sounds/accordion/notes/2.mp3",
    "AUDIO3": "sounds/accordion/notes/3.mp3",
    "AUDIO4": "sounds/accordion/notes/4.mp3",
    "AUDIO5": "sounds/accordion/notes/5.mp3",
    "AUDIO6": "sounds/accordion/notes/6.mp3",
    "AUDIO7": "sounds/accordion/notes/7.mp3",
    "AUDIO8": "sounds/accordion/notes/8.mp3",
    "RANGE_LOW": "F3",
    "RANGE_HIGH": "A6",
    "VIDEO0": "https://www.youtube.com/watch?v=CgCMBFcifVE",
    "VIDEO1": "https://www.youtube.com/watch?v=uhPhK57_Hbo",
    "VIDEO2": "https://www.youtube.com/watch?v=CjjeYX-6QHs",
    "THUMBNAIL0": "img/thumbnails/accordion_01.png",
    "THUMBNAIL1": "img/thumbnails/accordion_02.png",
    "THUMBNAIL2": "img/thumbnails/accordion_03.png",
    "TITLE0": "Atmosphere",
    "MUSIC0": "sounds/accordion/music/Atmosphere.mp3",
    "TITLE1": "Improvisation",
    "MUSIC1": "sounds/accordion/music/Improvisation.mp3",
    "TITLE2": "Improvisation2",
    "MUSIC2": "sounds/accordion/music/Improvisation2.mp3",
    "TAG1_STYLE": "",
    "TAG2_STYLE": "left:197px;",
    "RANGE_STYLE": "width: 58%;",
    "INSTRUMENT_PIC": "img/accordian1.png",
    "INTRODUCTION": "Accordions (from 19th century German Akkordeon) are a family of box-shaped musical instruments of the bellows-driven free-reed aerophone type, colloquially referred to as a squeezebox. (Wikipedia, 2017)."}
sax_dict = {
    "TITLE": "SAXOPHONE",
    "INSTRUMENT": "SAXOPHONE",
    "INSTRUMENTS": "class=\"selected\"",
    "AUDIO1": "sounds/sax/notes/1.mp3",
    "AUDIO2": "sounds/sax/notes/2.mp3",
    "AUDIO3": "sounds/sax/notes/3.mp3",
    "AUDIO4": "sounds/sax/notes/4.mp3",
    "AUDIO5": "sounds/sax/notes/5.mp3",
    "AUDIO6": "sounds/sax/notes/6.mp3",
    "AUDIO7": "sounds/sax/notes/7.mp3",
    "AUDIO8": "sounds/sax/notes/8.mp3",
    "RANGE_LOW": "D3",
    "RANGE_HIGH": "A5",
    "VIDEO0": "https://www.youtube.com/watch?v=-t9LjQdrMiM",
    "VIDEO1": "https://www.youtube.com/watch?v=jMe8uqoNZiQ",
    "VIDEO2": "https://www.youtube.com/watch?v=XLjK-7XCBfM",
    "THUMBNAIL0": "img/thumbnails/sax_01.png",
    "THUMBNAIL1": "img/thumbnails/sax_02.png",
    "THUMBNAIL2": "img/thumbnails/sax_03.png",
    "TITLE0": "Alto",
    "MUSIC0": "sounds/sax/music/Alto.mp3",
    "TITLE1": "Duduk",
    "MUSIC1": "sounds/sax/music/Duduk.mp3",
    "TITLE2": "Relaxing",
    "MUSIC2": "sounds/sax/music/Relaxing.mp3",
    "TAG1_STYLE": "left:42px;",
    "TAG2_STYLE": "left:146px;",
    "RANGE_STYLE": "margin-left: 20%; width: 50%;",
    "INSTRUMENT_PIC": "img/saxophone1.png",
    "INTRODUCTION": "The saxophone (also referred to as the sax) is a family of woodwind instruments. Saxophones are usually made of brass and played with a single-reed mouthpiece similar to that of the clarinet (Wikipedia, 2017)."}

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
