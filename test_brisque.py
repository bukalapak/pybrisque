# coding=utf-8
import os
import unittest

import numpy as np
import cv2

from utilities import root_path
from brisque import BRISQUE


class TestBRISQUE(unittest.TestCase):
    def setUp(self):
        self._distorted_path = root_path('examples','i04_14_1.bmp')

    def test_from_path(self):
        """Test directly from the path."""
        brisque = BRISQUE()
        self.assertAlmostEqual(
            brisque.get_score(self._distorted_path), 79.22545681241508)

    def test_from_image_rgb(self):
        image = cv2.imread(self._distorted_path)
        brisque = BRISQUE()
        self.assertAlmostEqual(
            brisque.get_score(image), 79.22545681241508)

    def test_from_grayscale(self):
        image = cv2.imread(self._distorted_path, 0)
        brisque = BRISQUE()
        self.assertAlmostEqual(
            brisque.get_score(image), 79.22545681241508)
