import config
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
  if os.path.exists(config.INSTALL_DIR):
    shutil.rmtree(config.INSTALL_DIR)
 
  copyAnything(configSys.ADDON_DIR, config.INSTALL_DIR)

def InstallAll():
  InstallAddon() 
