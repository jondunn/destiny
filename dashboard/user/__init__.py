# Copyright 2014 Daniel Reed <n@ml.org>

import json
import pprint
from base import bungie
from base.bungie import auth
from base.bungie.destiny import user as destiny_user
from dashboard import base_app


class MePage(base_app.RequestHandler):
  def get(self):
    self.response.render('dashboard/user/index.html', {
        'user': self.request.user,
        'user_info': bungie.GetCurrentUser(),
    })

  def post(self):
    try:
      bungled, bungleatk = auth.Auth(self.request.get('email'), self.request.get('password'))
    except:
      pass
    else:
      self.request.user.bungled = bungled
      self.request.user.bungleatk = bungleatk
      self.request.user.put()

    return self.redirect('/')


class UserHTMLPage(base_app.RequestHandler):
  def get(self, username):
    self.response.render('dashboard/user/character_sheet.html', {
        'breadcrumbs': (
            ('/' + username, username),
        ),
        'username': username,
    })


class UserJSONPage(base_app.RequestHandler):
  def get(self, username):
    user = destiny_user.User(username)
    self.response.content_type = 'application/json'
    self.response.write(json.dumps(user, sort_keys=True))


class UserPyPage(base_app.RequestHandler):
  def get(self, username):
    user = destiny_user.User(username)
    self.response.content_type = 'text/plain'
    self.response.write(pprint.pformat(user))


class UserRawPage(base_app.RequestHandler):
  def get(self, username):
    username, accounttype, accountid, summary = destiny_user.GetDestinyUser(username)
    self.response.content_type = 'text/html'
    self.response.render('dashboard/object.html', {
        'breadcrumbs': (
            ('/%s.raw' % username, username),
        ),
        'obj': summary,
    })


class Warmup(base_app.RequestHandler):
  def get(self):
    pass


app = base_app.WSGIApplication([
    ('/_ah/warmup', Warmup),
    ('/', MePage),
    ('/([a-zA-Z0-9-_ ]+)', UserHTMLPage),
    ('/([a-zA-Z0-9-_ ]+)[.]json', UserJSONPage),
    ('/([a-zA-Z0-9-_ ]+)[.]py', UserPyPage),
    ('/([a-zA-Z0-9-_ ]+)[.]raw', UserRawPage),
], debug=True)