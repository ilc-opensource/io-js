import os
from config import *
from util   import *

def GenOutputDirs():
  s = ''
  s += OUTPUT_COMP_PATH + ' '
  s += OUTPUT_DEV_PATH + ' '
  s += OUTPUT_SERVER_PATH + ' '
  s += OUTPUT_CMD_MAP_PATH + ' '
  return s

def GenShell():
  f = INC_MAKEFILE
  printDbg("generating " + f)
  fp = open(f, "w+")
  s = '''
OUTPUT_DIRS = %s %s
''' % (GenOutputDirs(), INC_MAKEFILE)
  fp.write(s)
