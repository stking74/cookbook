#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:54:21 2022

@author: tyler
"""

import os
import hashlib
import json

class Recipie:
    
    def __init__(self):
        return

class File:

    def __init__(self, filename, gethash=False):

        self.long_name = None
        self.short_name = None
        self.location = None
        self.extension = None
        self.size = None
        self.tags = []

        if not os.path.isabs(filename):
            filename = os.path.asabs(filename)

        self.long_name = filename
        self.location, self.short_name = os.path.split(filename)

        try:
            self.extension = self.short_name.split('.')[-1]
        except IndexError:
            print(f'Could not identify file extension for file {filename}')
        try:
            self.size = os.path.getsize(self.long_name)
        except:
            print(f'Could not get file size for {self.long_name}')  
        return
    
    def add_tag(self, tag):
        if tag in self.tags:
            print(f'File {self.long_name} already tagged "{tag}".')
        else:
            self.tags.append(tag)
        return
    
    def remove_tag(self, tag):
        if tag not in self.tags:
            print(f'Tag "{tag}" not found for file {self.long_name}.')
        else:
            self.tags.remove(tag)
        return

    def gethash(self, buffersize=2**20):
        '''
        Calculate SHA-256 hash of file.

        Parameters
        ----------
        buffersize : int, optional
            Size of buffer for digesting file, in bytes. The default is 2**20.

        Returns
        -------
        self.hash : str
            SHA-256 hash of file.
        '''
        hasher = hashlib.sha256()
        
        block = [None]
        with open(self.long_name, 'rb') as f:
            while len(block) > 0:
                block = f.read(buffersize)
                hasher.update(block)
        self.hash = hasher.hexdigest()
        return self.hash

    @staticmethod
    def fromdict(dictionary):
        '''
        Generates File object from metadata dictionary.

        Parameters
        ----------
        dictionary : dict
            Dictionary containing file metadata.

        Returns
        -------
        file : File
            Reconstituted File object.

        '''
        fullname = dictionary['fullname']
        file = File(fullname)
        file.size = dictionary['size']
        file.hash = dictionary['hash']
        file.last_mofified = dictionary['modified']
        file.last_accessed = dictionary['accessed']
        file.ctime = dictionary['created']
        file.tags = dictionary['tags']

        return file

    def delete_file(self):
        '''
        Deletes the file from filesystem (if it exists).
        '''
        try:
            os.remove(self.long_name)
        except OSError:
            print(f'WARNING:File {self.fullname} could not be deleted!')
        return

class Book(dict):

    def __init__(self, root, gethash=False, filters=[]):
        return

if __name__ == '__main__':
    pass
