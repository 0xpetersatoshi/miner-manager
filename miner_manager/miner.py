"""
Functions for toggling the miner on/off
"""
import subprocess

import psutil

PROCESS_NAME = 't-rex.exe'
BAT_FILEPATH = 'ETH-ethermine.bat'

def miner_is_on() -> bool:
    """Determines if miner .exe is running"""
    if PROCESS_NAME in (p.name() for p in psutil.process_iter()):
        return True
    
    return False


def toggle_miner_on_off():
    """Toggles the miner program on/off"""
    if miner_is_on():
        # Turn miner off
        for proc in psutil.process_iter():
            if proc.name() == PROCESS_NAME:
                proc.kill()
    else:
        # Turn miner on if not running
        subprocess.call([BAT_FILEPATH])
