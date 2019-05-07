#!/usr/bin/env python
# -*- encoding: utf-8 -*-



import http_helper as http

_kPaths = {
    # post
    'open': '/api/accounts/open',
    # post
    'open2': '/api/accounts/open2',
    # get
    'getBalance': '/api/accounts/getBalance',
    # get
    'getPublicKey': '/api/accounts/getPublicKey',
    # post
    'generatePublicKey': '/api/accounts/generatePublicKey',
    # get
    'getDelegates': '/api/accounts/delegates',
    # get
    'getDelegateFee': '/api/accounts/delegates/fee',
    # put
    'addDelegates': '/api/accounts/delegates',
    # get
    'getAccount': '/api/accounts',
    # get
    'newAccount': '/api/accounts/new',
    # get
    'accountOnChain': '/api/accounts/effectivity',
    # get
    'delayOrders': '/api/accounts/delayOrders',
    # get
    'top': '/api/accounts/top',
    # get
    'count': '/api/accounts/count'
}


def open(nodeServer, secret, timeout=4000):
    # TODO: check argumens
    return http.post(nodeServer+_kPaths['open'], {'secret': secret}, timeout=timeout)


def open2(nodeServer, publicKey, timeout=4000):
    # TODO: check arguments
    return http.post(nodeServer+_kPaths['open2'], {'publicKey': publicKey}, timeout=timeout)

def getBalance(nodeServer, address, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getBalance'], {'address': address}, timeout=timeout)


def getPublicKey(nodeServer, address, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getPublicKey'], {'address': address}, timeout=timeout)


def generatePublicKey(nodeServer, secret, timeout=4000):
    # TODO: check arguments
    return http.post(nodeServer+_kPaths['generatePublicKey'], {'secret': secret}, timeout=timeout)


def getDelegates(nodeServer, address, timeout=4000):
    # TODO: check arugments
    return http.get(nodeServer+_kPaths['getDelegates'], {'address': address}, timeout=timeout)


def getDelegateFee(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getDelegateFee'], timeout=timeout)


def addDelegates(nodeServer, secret, add=None, remove=None, publicKey=None, secondSecret=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {}   #把请求内容全部放到字典里
    delegates = []  #代理人列表类型是数组
    if add != None:
        delegates.append('+' + add)
    if remove != None:
        delegates.append('-'+remove)
    assert len(delegates) > 0, "delegates is empty"
    # assert(len(delegates) > 0, "delegates is empty.")
    reqArgs['secret'] = secret
    reqArgs['delegates'] = delegates
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    return http.put(nodeServer+_kPaths['addDelegates'], reqArgs, timeout=timeout)


def getAccount(nodeServer, address, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getAccount'], {'address': address}, timeout=timeout)


def new(nodeServer, ent=128, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['newAccount'], {'ent': ent}, timeout=timeout)


def accountOnChain(nodeServer, address, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['accountOnChain'], {'address': address}, timeout=timeout)


def delayOrders(nodeServer, address, mode=0, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['delayOrders'], {'address': address, 'mode': mode}, timeout=timeout)


def top(nodeServer, offset=0, limit=100, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['top'], {'offset': offset, 'limit': limit}, timeout=timeout)


def count(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['count'], None, timeout=timeout)
