from config  import *
from util import *
import shutil, errno
import os

def copyAnything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def InstallAddon():
  if os.path.exists(INSTALL_DIR):
    shutil.rmtree(INSTALL_DIR)
 
  copyAnything(ADDON_DIR, INSTALL_DIR)

def InstallAll():
  InstallAddon() 
