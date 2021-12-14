#!/usr/bin/env python3
from twisted.internet import reactor

from ote import Ote
from dateutil import parser

prices_1 = {}
prices_2 = {}


def _prices_scraped_1(prices):
    global prices_1
    prices_1 = prices
    return prices


def _prices_scraped_2(prices):
    global prices_2
    prices_2 = prices
    return prices


date_from = parser.parse('2021-09-23').date()
date_to = parser.parse('2021-09-24').date()
date_to2 = parser.parse('2021-09-25').date()

ote = Ote()

deferred_prices_1 = ote.getDayMarketPrices(date_from, date_to)
deferred_prices_1.addCallback(_prices_scraped_1)

deferred_prices_2 = ote.getDayMarketPrices(date_to, date_to2)
deferred_prices_2.addCallback(_prices_scraped_2)

d = ote.join()
d.addBoth(lambda _: reactor.stop())

reactor.run(installSignalHandlers=False)  # the script will block here until the crawling is finished

print(prices_1)
print(prices_2)
