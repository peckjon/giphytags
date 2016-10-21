import json
import webapp2
import urllib2
import re

class GiphytagHandler(webapp2.RequestHandler):

    def post(self):
        id = json.loads(self.request.body).get('id',None)
        if not id:
            return self.response.write('Invalid ID')
        url = "https://giphy.com/gifs/%s" % id
        try:
            response = urllib2.urlopen(url)
            html = response.read()
            tags = re.search('<meta name="keywords" content="(.*)"', html)
            return self.response.write(tags.group(1).replace(', GIF','').replace(', Animated GIF',''))
        except:
            return self.response.write('Could not get keyword tags from '+url)

app = webapp2.WSGIApplication([
    ('/json/giphytags', GiphytagHandler),
], debug=True)