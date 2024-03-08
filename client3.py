################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    # this returns the average of the top_ask and top_bid price
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):  # this function is being called by the main fucntion
    """ Get ratio of price_a and price_b """
    """This function's been updated to return the actual ratio of the price_a and price_b instead of just returning one"""
    if (price_b == 0):  # insted of returning 1 by default we returning the actual ratio of the prices
        return

    return price_a/price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(
            QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        prices = {}  # we can iterate through prices
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            # stock is used an index to identify the stock prices of stock
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" %
                  (stock, bid_price, ask_price, price))

        # we get the ratio of the stock "ABC" and "DEF"
        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
