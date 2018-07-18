from google.appengine.ext import ndb

class Meme(ndb.Model):
    first_line = ndb.StringProperty(required=True)
    second_line = ndb.StringProperty(required=False)
    pic_type = ndb.StringProperty(required=False)

    def get_meme_url(self):
        return "../images/%s.jpg" % self.pic_type
