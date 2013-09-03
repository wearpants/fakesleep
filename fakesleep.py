"""provides a fake sleep() for use in tests"""

import time as time_mod

originals = {name: getattr(time_mod, name) for name in
             ['time', 'sleep', 'gmtime', 'localtime', 'ctime', 'asctime', 'strftime']}

epoch = None #: the fake current time

def reset(seconds=None):
    """reset the global fake time to the real current time

    :arg float seconds: fake current time, in seconds since the epoch. If None, use the real current time.
    """
    global epoch
    epoch = seconds if seconds is not None else originals['time']()

reset()

def time():
    return epoch

def sleep(seconds):
    global epoch
    epoch += seconds

def gmtime(seconds=None):
    return originals['gmtime'](seconds if seconds is not None else epoch)

def localtime(seconds=None):
    return originals['localtime'](seconds if seconds is not None else epoch)

def ctime(seconds=None):
    return originals['ctime'](seconds if seconds is not None else epoch)

def asctime(t=None):
    return originals['asctime'](t if t is not None else localtime())

def strftime(format, t=None):
    return originals['strftime'](format, t if t is not None else localtime())    

def monkey_patch():
    """monkey patch `time` module to use out versions"""
    reset()
    time_mod.time = time
    time_mod.sleep = sleep
    time_mod.gmtime = gmtime
    time_mod.localtime = localtime
    time_mod.ctime = ctime
    time_mod.asctime = asctime
    time_mod.strftime = strftime

def monkey_restore():
    """restore real versions. Inverse of `monkey_patch`"""
    for k, v in originals.items():
        setattr(time_mod, k, v)
    
    global epoch
    epoch = None