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
