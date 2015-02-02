# Copyright 2014 Daniel Reed <n@ml.org>

import logging
from google.appengine.ext import ndb
from base.bungie import platform
from base.bungie.destiny import definitions
import destiny


class DestinyPGCR(ndb.Model):
  activityid = ndb.IntegerProperty()
  report = ndb.JsonProperty()


class CachingBungie(platform.Bungie):
  def DestinyStatsPostGameCarnageReport(self, activityid):
    pgcr = DestinyPGCR.query(DestinyPGCR.activityid == activityid).get()
    if pgcr:
      return pgcr.report
    report = super(CachingBungie, self).DestinyStatsPostGameCarnageReport(activityid=activityid)
    logging.info('Caching activity %r.', activityid)
    DestinyPGCR(activityid=activityid, report=report).put()
    return report


BUNGIE = CachingBungie()
DEFS = definitions.Definitions(bungie=BUNGIE)


class DestinyUser(ndb.Model):
  account = ndb.StringProperty()
  name = ndb.StringProperty()
  accounttype = ndb.IntegerProperty()
  accountid = ndb.IntegerProperty()

  @classmethod
  def GetUser(cls, username):
    destiny_user = cls.query(cls.account == username.lower()).get()

    if destiny_user:
      user = destiny.User(destiny_user.name, accounttype=destiny_user.accounttype,
                          accountid=destiny_user.accountid, bungie=BUNGIE, defs=DEFS)
    else:
      user = destiny.User(username, bungie=BUNGIE, defs=DEFS)
      cls(account=username.lower(), name=user['name'], accounttype=user['account_type'], 
          accountid=user['account_id']).put()

    return user
