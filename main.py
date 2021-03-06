# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

def getImageForMemeType(meme_type):
    return "../images/%s.jpg" % meme_type
    # if meme_type == 'old-class':
    #     return 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    # elif meme_type == 'college-grad':
    #     return 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    # elif meme_type == 'thinking-ape':
    #     return 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    # else:
    #     return 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'

class EnterInfoPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = \
                jinja_current_directory.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

class MemeResultPage(webapp2.RequestHandler):
    def post(self):
        result_template = \
                jinja_current_directory.get_template('templates/result.html')

        line_1 = self.request.get('user-first-ln')
        line_2 = self.request.get('user-second-ln')
        meme_type = self.request.get('meme-type')

        template_dict = {
            'line1': line_1,
            'line2': line_2,
            # Find a good image url for the meme_type
            'image_url': getImageForMemeType(meme_type)
        }

        self.response.write(result_template.render(template_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoPage),
    ('/memeresult', MemeResultPage),
], debug=True)
