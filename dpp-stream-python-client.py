#!/usr/bin/python
from socketIO_client import SocketIO
#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://streams.dapowerplay.com'
api_key = 'place your public api key here'
api_secret = 'place your secret api key here'
socket_io = SocketIO(url, 443, forceNew=True, params={'apikey': api_key,
                                                    'apisecret': api_secret})
subscription = [{'product': '*'}]

def on_error(*args):
    print('error', args)


def on_connect():
    print('connect')
    socket_io.emit('streams', on_streams_response)
    socket_io.wait_for_callbacks()


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')
    on_connect()


def on_streams_response(*args):
    socket_io.emit('subscribe', subscription)


def on_trades(*args):
    print('on_trades', args)


def on_orderbook_lv1(*args):
    print('on_orderbook_lv1', args)


def on_orderbook_lv2(*args):
    print('on_orderbook_lv2', args)


def on_indices(*args):
    print('on_indices', args)

def on_sentiments(*args):
    print('on_sentiments', args)


def on_candels(*args):
    print('on_candles', args)


def on_news(*args):
    print('on_news', args)

def on_technical_indicators(*args):
    print('on_technical_indicators', args)


def main():

    socket_io.on('connect', on_connect)
    socket_io.on('disconnect', on_disconnect)
    socket_io.on('reconnect', on_reconnect)
    socket_io.on('trades', on_trades)
    socket_io.on('orderbooks_lv1', on_orderbook_lv1)
    socket_io.on('orderbooks_lv2', on_orderbook_lv2)
    socket_io.on('indices', on_indices)
    socket_io.on('sentiments', on_sentiments)
    socket_io.on('candles', on_candels)
    socket_io.on('news', on_news)
    socket_io.on('technical_indicators', on_technical_indicators)
    socket_io.on('error', on_error)
    socket_io.wait()


if __name__ == "__main__":
    main()