import os
import configSys
from util   import *

def GenOutputDirs():
  s = ''
  s += configSys.OUTPUT_COMP_PATH + ' '
  s += configSys.OUTPUT_DEV_PATH + ' '
  s += configSys.OUTPUT_SERVER_PATH + ' '
  s += configSys.OUTPUT_CMD_MAP_PATH + ' '
  return s

def GenShell():
  f = configSys.INC_MAKEFILE
  printDbg("generating " + f)
  fp = open(f, "w+")
  s = '''
OUTPUT_DIRS = %s %s
''' % (GenOutputDirs(), configSys.INC_MAKEFILE)
  fp.write(s)
