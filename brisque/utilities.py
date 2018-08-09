# coding=utf-8
import os


def root_path(*args):
    """Get the path to the project root.

    :param args : List of path elements e.g. ['data', 'data.csv']

    :return: Absolute path to the asked path.
    """
    path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
    for item in args:
        path = os.path.abspath(os.path.join(path, item))

    return path
