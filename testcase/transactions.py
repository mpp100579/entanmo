#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import http_helper as http

_kPaths = {
    # get
    'getTransaction': '/api/transactions/get',
    # get
    'getTransactions': '/api/transactions',
    # get
    'getUnconfirmedTransaction': '/api/transactions/unconfirmed/get',
    # get
    'getUnconfirmedTransactions': '/api/transactions/unconfirmed',
    # put
    'add': '/api/transactions',
    # put
    'addDelay': '/api/transactions/delay'
}


def getTransaction(nodeServer, trid, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getTransaction'], {'id': trid}, timeout=timeout)


def getTransactions(nodeServer, offset=0, limit=100, aType=None, senderId=None, senderPublicKey=None, recipientId=None, ownerPublicKey=None, ownerAddress=None, orderBy=None, amount=None, fee=None, currency=None, aAnd=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'offset': offset, 'limit': limit}
    if aType != None:
        reqArgs['type'] = aType
    if senderId != None:
        reqArgs['senderId'] = senderId
    if senderPublicKey != None:
        reqArgs['senderPublicKey'] = senderPublicKey
    if recipientId != None:
        reqArgs['recipientId'] = recipientId
    if ownerPublicKey != None:
        reqArgs['ownerPublicKey'] = ownerPublicKey
    if ownerAddress != None:
        reqArgs['ownerAddress'] = ownerAddress
    if orderBy != None:
        reqArgs['orderBy'] = orderBy
    if amount != None:
        reqArgs['amount'] = amount
    if fee != None:
        reqArgs['fee'] = fee
    if currency != None:
        reqArgs['currency'] = currency
    if aAnd != None:
        reqArgs['and'] = aAnd
    return http.get(nodeServer+_kPaths['getTransactions'], reqArgs, timeout=timeout)


def getUnconfirmedTransaction(nodeServer, trid, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getUnconfirmedTransaction'], {'id': trid}, timeout=timeout)


def getUnconfirmedTransactions(nodeServer, senderPublicKey=None, address=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {}
    if senderPublicKey != None:
        reqArgs['senderPublicKey'] = senderPublicKey
    if address != None:
        reqArgs['address'] = address
    assert len(reqArgs) > 0, 'Invalid arguments'
    return http.get(nodeServer+_kPaths['getUnconfirmedTransactions'], reqArgs, timeout=timeout)


def add(nodeServer, secret, recipientId, amount, publicKey=None, secondSecret=None, message=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'secret': secret, 'recipientId': recipientId, 'amount': amount}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    if message != None:
        reqArgs['message'] = message
    print('转账交易')
    return http.put(nodeServer+_kPaths['add'], reqArgs, timeout=timeout)





def addDelay(nodeServer, secret, recipientId, amount, delayTimestamp, publicKey=None, secondSecret=None, message=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'secret': secret, 'recipientId': recipientId,
               'amount': amount, 'args': [''+delayTimestamp]}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    if message != None:
        reqArgs['message'] = message
    return http.put(nodeServer+_kPaths['addDelay'], reqArgs, timeout=timeout)
