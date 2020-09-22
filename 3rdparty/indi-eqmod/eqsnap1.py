#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import stat
import select
import time

PIPE_FILE='/tmp/eqsnapport1'
try:
    s=os.stat(PIPE_FILE)
    if not stat.S_ISFIFO(s.st_mode):
        import sys
        print("eqsnapport1: " + PIPE_FILE + " exists and is NOT a FIFO.")
        print("Please change PIPE_FILE in this script. Aborting.")
        sys.exit(1) 
except FileNotFoundError:
    os.mkfifo(PIPE_FILE)

poll = select.poll()
try:
    while True:
        f=open(PIPE_FILE, 'r')
        os.system("indi_setprop -s 'EQMod Mount.SNAPPORT1.SNAPPORT1_ON=On;SNAPPORT1_OFF=Off'")
        #print(time.asctime() + ": indi_setprop -s 'EQMod Mount.SNAPPORT1.SNAPPORT1_ON=On;SNAPPORT1_OFF=Off'")
        #rlist, wlist, xlist=[f], [], []
        #rready, wready, eready = select.select(rlist, wlist, xlist)
        poll.register(f, select.POLLHUP)
        poll.poll()
        poll.unregister(f)
        os.system("indi_setprop -s 'EQMod Mount.SNAPPORT1.SNAPPORT1_ON=Off;SNAPPORT1_OFF=On'")
        #print(time.asctime() + ": indi_setprop -s 'EQMod Mount.SNAPPORT1.SNAPPORT1_ON=Off;SNAPPORT1_OFF=On'")
except KeyboardInterrupt:
    pass

os.unlink(PIPE_FILE)
