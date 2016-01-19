#!/usr/bin/env python
#
# -*- mode:python; sh-basic-offset:4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim:set tabstop=4 softtabstop=4 expandtab shiftwidth=4 fileencoding=utf-8:
#
# Copyright 2013, Jorge Gallegos <kad@blegh.net>

"""
The ``basicrack`` application will hold all methods related to management of
basicrack locations in clusto.
"""

from bottle import route, get, request
import clusto
from clusto import drivers
from clustoapi import util


def _is_integer(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

def _get_basicrack(basicrack):
    "A wrapper because an extra check has to be made :("

    obj, status, msg = util.get(basicrack)
    if obj:
        if not issubclass(obj.__class__, drivers.locations.BasicRack):
            msg = 'The object "%s" is not a basicrack' % (basicrack,)
            status = 409
            obj = None
        else:
            pass
    else:
        pass

    return obj, status, msg


@get('/basicrack/<rack>/<rackU>')
@get('/basicrack/<rack>/get-device-in/<rackU>')
def get_device_in(rack=None, rackU=None):
    """
Gets the device in ``rackU`` of ``rack``

Examples:

.. code:: bash

    $ ${get} ${server_url}/basicrack/basicrack1/1
    HTTP: 200
    Content-type: application/json

The above will get the device in RU "1" of "basicrack1"
"""

    obj, status, msg = _get_basicrack(rack)
    if not obj:
        return util.dumps(msg, status)
    else:
        return util.dumps(util.show(obj))

    result = []

'''
    try:
        ents = clusto.get_entities(clusto_drivers=[driver])
    except NameError as ne:
        return util.dumps(
            'Not a valid driver "%s" (%s)' % (driver, ne,), 404
        )

    for ent in ents:
        result.append(util.unclusto(ent))

    return util.dumps(result)
'''
