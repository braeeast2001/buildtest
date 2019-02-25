############################################################################
#
#  Copyright 2017-2019
#
#   https://github.com/HPC-buildtest/buildtest-framework
#
#  This file is part of buildtest.
#
#    buildtest is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    buildtest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with buildtest.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################
"""
This python module provides some generic file level operation such as creating
file, and directory and strip hidden file character. This module also
provides function to update log file, check if file is hidden and determine
if a string is found in file
"""
import os
import logging

from buildtest.tools.config import logID
from buildtest.tools.log import BuildTestError


def isFile(file):
    if not os.path.isfile(file):
        raise BuildTestError("Invalid File Path %s. "  % file)


def isDir(dir):
    if not os.path.isdir(dir):
        raise BuildTestError("Invalid Directory Path %s" % dir)
    return True


def walk_tree(root_dir,ext):
    """ traverse a directory tree and return list of files based on extension type"""
    list_files = []
    isDir(root_dir)
    for root, subdir, files in os.walk(root_dir):
        for file in files:
            if file.endswith(ext):
               list_files.append(os.path.join(root,file))

    return list_files


def walk_tree_multi_ext(root_dir,ext_list):
    """ traverse a directory tree and return list of files based on extension type where
    extension is a list as pose to a single string """
    list_files = []
    isDir(root_dir)
    for root, subdir, files in os.walk(root_dir):
        for file in files:
            # return a list of True, False based on file extension
            ext_bool_list = [file.endswith(ext) for ext in ext_list]
            if any(ext_bool_list):
               list_files.append(os.path.join(root,file))

    return list_files


def stripHiddenFile(file):
    """  removes the leading "." character from file """
    file=file[1:]
    return file


def create_file(filename):
    """ Create an empty file if it doesn't exist   """
    logger = logging.getLogger(logID)
    if not os.path.isfile(filename):
        try:
            fd=open(filename,'w')
            logger.debug("Creating File: %s", filename)
            fd.close()
        except OSError as err:
            print (err)


def create_dir(dirname):
    """Create directory if it doesn't exist"""
    logger = logging.getLogger(logID)
    if not os.path.isdir(dirname):
        try:
            os.makedirs(dirname)
            logger.debug("Creating Directory: %s", dirname)
        except OSError as err:
            print (err)
            raise


def string_in_file(string,filename):

    """ returns true/false to indicate if string is in file """
    if string in open(filename).read():
        return True
    else:
        return False