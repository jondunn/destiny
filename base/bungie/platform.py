#!/usr/bin/python
#
# Copyright 2014 Daniel Reed <n@ml.org>

import urlparse
from base.util import fetch


class Bungie(object):
  base = 'https://www.bungie.net/platform/'

  def Fetch(self, suffix, *args, **kwargs):
    if args:
      suffix %= args
    elif kwargs:
      suffix %= kwargs

    url = urlparse.urljoin(self.base, suffix)

    if '?' in url:
      url += '&'
    else:
      url += '?'
    url += 'definitions=true'

    data = fetch.Fetch(url)
    if isinstance(data, dict):
      if data.get('ErrorStatus') == 'Success':
        return data['Response']
    else:
      return data