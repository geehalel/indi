#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import select

PIPE_FILE='/tmp/eqsnapport1'
os.mkfifo(PIPE_FILE)

try:
    while True:
        f=open(PIPE_FILE, 'r')
        os.system("indi_setprop -s 'EQMod Mount.SNAPPORT1.SNAPPORT1_ON=On;SNAPPORT1_OFF=Off'")
        rlist, wlist, xlist=[f], [], []
        rready, wready, eready = select.select(rlist, wlist, xlist)
        os.system("indi_setprop -s 'EQMod Mount.SNAPPORT1.SNAPPORT1_ON=Off;SNAPPORT1_OFF=On'")
except KeyboardInterrupt:
    pass

os.unlink(PIPE_FILE)

        
