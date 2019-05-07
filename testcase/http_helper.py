#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import json

"""
A http cilent for get, post, put methods
"""

# _headers = {'Content-Type': 'application/json'}
_headers = {}
# _jsonDecoder = json.JSONDecoder()


def get(url, params=None, timeout=4000):
    '''
    A get method for request to entanmo node
    '''

    try:
        if params == None:
            r = requests.get(url, headers=_headers, timeout=timeout/1000)
        else:
            r = requests.get(url, headers=_headers,
                             timeout=timeout/1000, params=params)

        if r.status_code == 200 or r.status_code == 500:
            # data = _jsonDecoder.decode(r.content)
            data = json.loads(r.content)
            if data['success'] == True:
                del data['success']
                return data
            else:
                return {'done': False, 'error': data['error']}
        else:
            return {'done': False, 'error': r.reason}

    except Exception as e:
        return {'done': False, 'error': e.message}

def put(url, body=None, timeout=4000):
    '''
    A put method for request to entanmo node
    '''

    try:
        if body == None:
            r = requests.put(url, headers=_headers, timeout=timeout/1000)
        else:
            r = requests.put(url, headers=_headers,
                             timeout=timeout/1000, json=body)

        if r.status_code == 200 or r.status_code == 500:
            # data = _jsonDecoder.decode(r.content)
            data = json.loads(r.content)
            if data['success'] == True:
                del data['success']
                return {'done': True, 'data': data}
            else:
                return {'done': False, 'error': data['error']}
        else:
            return {'done': False, 'error': r.reason}

    except Exception as e:
        return {'done': False, 'error': e.message}


def post(url, body=None, timeout=4000):
    '''
    A post method for request to entanmo node
    '''

    try:
        if body == None:
            r = requests.post(url, headers=_headers, timeout=timeout/1000)
        else:
            r = requests.post(url, headers=_headers,
                              timeout=timeout/1000, json=body)
        if r.status_code == 200 or r.status_code == 500:
            # data = _jsonDecoder.decode(r.content)
            data = json.loads(r.content)
            if data['success'] == True:
                del data['success']
                return {'done': True, 'data': data}
            else:
                return {'done': False, 'error': data['error']}
        else:
            return {'done': False, 'error': r.reason}

    except Exception as e:
        return {'done': False, 'error': e.message}
