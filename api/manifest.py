#!/usr/bin/env python

import uuid
import os
import tempfile
import zipfile

class Manifest:
   def generateUUID(self):
      return uuid.uuid4()

   def getFullExport(self):
      tmpDir = tempfile.mkdtemp(suffix='', prefix='', dir=None)
      basedir = os.path.abspath(tmpDir)

   def addFilestoArchive(self):
      pass

   def addFiletoArchive(self):
      pass




