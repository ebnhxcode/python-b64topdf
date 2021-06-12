#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
with open('b64.dat', 'r') as docs:
    for idx, b64 in enumerate(docs):
        bytes = base64.b64decode(b64)
        if bytes[0:4] != b'%PDF':
            raise ValueError('No se pudo obtener la firma del formato PDF en el archivo.')
        f = open('file_{}.pdf'.format(idx), 'wb')
        f.write(bytes)
        f.close()