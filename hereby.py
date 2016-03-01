# coding: utf-8

# Copyright (c) 2016 "Hugo Herter http://hugoherter.com"
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path


class Here(object):
    """Create an object that gives you access to files relative to the current
    Python file.

    Usage:
    >>> from here import Here
    >>> here = Here(__file__)
    >>> f = here.open('somefile.txt').read()
    """

    def __init__(self, python_file_path):
        self.path = python_file_path

    def open(self, path, mode='r', *args, **kwargs):
        """Proxy to function `open` with path to the current file."""
        return open(os.path.join(os.path.dirname(self.path), path),
                    mode=mode, *args, **kwargs)
