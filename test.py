#!/usr/bin/env python3
import json

from ote import Ote
from dateutil import parser

ote = Ote()
date_from = parser.parse('2021-09-23').date()
date_to = parser.parse('2021-09-24').date()
prices = ote.getDayMarketPrices(date_from, date_to)
print(json.dumps(prices))
