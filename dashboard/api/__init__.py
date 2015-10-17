# Copyright 2015 Daniel Reed <n@ml.org>

from base import bungie
from base.bungie import destiny
from dashboard import base_app


ENDPOINTS = {
    'GetAccountSummary': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
    ),
    'GetActivityHistory': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
        ('mode', 'text', 'None', 'mode',
         'The game mode: AllArena, AllPvE, AllPvP, AllStrikes, Arena, ArenaChallenge, Control, '
         'Elimination, FreeForAll, Heroic, IronBanner, Lockdown, Mayhem, Nightfall, None, Patrol, '
         'PvPIntroduction, Raid, Rift, Story, Strike, Team, ThreeVsThree, TrialsOfOsiris, or '
         'ZoneControl. "None" returns all activities.'),
        ('count', 'number', 250, 'count',
         'The number of results to return (1 - 250).'),
        ('page', 'number', 0, 'page',
         'The page offset.'),
    ),
    'GetAdvisorsForCurrentCharacter': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetAllItemsSummary': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
    ),
    'GetAvailableLocales': (),
    'GetCharacter': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetCharacterActivities': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetCharacterInventory': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetCharacterProgression': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetCharacterSummary': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetCurrentUser': (),
    'GetDestinyAggregateActivityStats': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 2305843009223046587, 'characterId',
         'The code for the character to inspect.'),
    ),
    'GetDestinyManifest': (),
    'GetItemDetail': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('accountid', 'number', 4611686018436064455, 'destinyMembershipId',
         'The numeric membership code.'),
        ('charid', 'number', 0, 'characterId',
         'The code for the character to inspect. 0 for items in the vault.'),
        ('itemid', 'number', 0, 'itemInstanceId',
         'The code for a specific instance of an item. Always 0 for stackable items.'),
    ),
    'GetMyGrimoire': (
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
    ),
    'GetPostGameCarnageReport': (
        ('activityid', 'number', 3966013892, 'activityId',
         "The activity's instanceId."),
    ),
    'GetPublicAdvisors': (),
    'GetPublicXurVendor': (),
    'HelloWorld': (),
    'SearchDestinyPlayer': (
        ('username', 'text', None, 'displayName',
         'The Bungie.net username to search for.'),
    ),
    'Settings': (),
    'TransferItem': (
        ('hash', 'number', None, 'itemReferenceHash',
         'The manifest code for all items with the same name.'),
        ('id', 'number', 0, 'itemId',
         'The code for a specific instance of an item. Always 0 for stackable items.'),
        ('quantity', 'number', 1, 'stackSize',
         'The number of items to transfer. Always 1 for non-stackable items.'),
        ('accounttype', 'number', 2, 'membershipType',
         'The numeric membership type (1 = XBL, 2 = PSN).'),
        ('from', 'text', None, 'characterId',
         'The code for the character to take the item from. Empty when taking from the vault.'),
        ('to', 'text', None, 'characterId',
         'The code for the character to give the item to. Empty when storing in the vault.'),
    ),
}


class Index(base_app.RequestHandler):
  def get(self):
    self.response.render('dashboard/api/index.html', {
        'breadcrumbs': (
            ('/api/', 'Bungie.net Platform API'),
        ),
        'endpoints': ENDPOINTS,
    })


class Generic(base_app.RequestHandler):
  def get(self, callname):
    data = ENDPOINTS.get(callname)
    if data is None:
      return self.error(404)
    args = []
    for param, type, default, name, desc in data:
      arg = self.request.get(param)
      if type == 'number':
        arg = long(arg)
      args.append(arg)
    method = getattr(destiny, callname, None) or getattr(bungie, callname)
    self.response.content_type = 'text/html'
    self.response.render('dashboard/object.html', {
        'breadcrumbs': (
            ('/api/', 'Bungie.net Platform API'),
            ('/api/' + callname, callname),
        ),
        'obj': method(*args),
    })

  post = get


class TransferItem(base_app.RequestHandler):
  def post(self):
    item_hash = self.request.get('hash')
    item_id = self.request.get('id')
    quantity = long(self.request.get('quantity'))
    accounttype = int(self.request.get('accounttype'))
    from_char = self.request.get('from')
    to_char = self.request.get('to')
    if from_char:
      destiny.TransferItem(accounttype, from_char, item_hash, item_id, quantity, True)
      print 'Transferred from %r to Vault.' % from_char
    if to_char:
      destiny.TransferItem(accounttype, to_char, item_hash, item_id, quantity, False)
      print 'Transferred from Vault to %r.' % to_char
    self.response.write('1')


app = base_app.WSGIApplication([
    ('/api/?', Index),
    ('/api/TransferItem/?', TransferItem),
    ('/api/(.*)/?', Generic),
], debug=True)