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
OUTPUT_DIRS = %s
''' % (GenOutputDirs())

  s += '''
OUTPUT_FILES = %s %s %s
''' % (GYP_PATH + GYP_FILE, GYP_PATH + Global_CLASS_VAR_FILE, INC_MAKEFILE)
  fp.write(s)
