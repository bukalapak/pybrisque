# coding=utf-8
import unittest

import numpy as np
import cv2

from brisque import BRISQUE
from brisque.utilities import root_path


class TestBRISQUE(unittest.TestCase):
    def setUp(self):
        self._distorted_path = root_path('examples','i04_14_1.bmp')
        # These feature are extracted from the original Matlab code of the
        # distorted image above (
        # https://github.com/dsoellinger/blind_image_quality_toolbox/tree/master/%2Bbrisque)

        self._brisque_feat = np.array([
            2.187000, 0.305119, 0.731000, 0.046159, 0.078954, 0.124348,
            0.735000, 0.032419, 0.086307, 0.118338, 0.733000, -0.020298,
            0.112611, 0.092477, 0.730000, -0.022557, 0.114732, 0.092231,
            2.103000, 0.360946, 0.731000, -0.055774, 0.183185, 0.116578,
            0.734000, -0.046589, 0.179101, 0.123198, 0.730000, -0.037948,
            0.168773, 0.123828, 0.725000, -0.033253, 0.165621, 0.126170
        ])
        self._scaled_feat = np.array([
            -0.617264, -0.270555, -0.295875, 0.0406103, -0.778699, -0.474667,
            -0.297065, 0.0308621, -0.757414, -0.500593, -0.258806,
            -0.0243801, -0.671236, -0.656588, -0.275518, -0.00898751,
            -0.665791, -0.658926, 0.168636, 0.00856362, 0.23913, -0.72301,
            -0.171255, -0.433049, 0.24878, -0.502953, -0.193939, -0.392484,
            0.308192, -0.264632, -0.365476, -0.333965, 0.304462, -0.19329,
            -0.375196, -0.322727])
        # The expected score from Matlab
        self._expected_score = 52.521

    def test_from_path(self):
        """Test directly from the path."""
        brisque = BRISQUE()
        self.assertAlmostEqual(
            brisque.get_score(self._distorted_path), 50.2686, places=3)

    def test_from_image_rgb(self):
        image = cv2.imread(self._distorted_path)
        brisque = BRISQUE()
        self.assertAlmostEqual(
            brisque.get_score(image), 50.2686, places=3)

    def test_from_grayscale(self):
        image = cv2.imread(self._distorted_path, 0)
        brisque = BRISQUE()
        self.assertAlmostEqual(
            brisque.get_score(image), 50.2686, places=3)

    def test_score_from_scaled_feature(self):
        """Test score from scaled feature from Matlab original code."""
        brisque = BRISQUE()
        score = brisque._calculate_score(self._scaled_feat)
        self.assertAlmostEqual(score, 52.52, places=2)

    def test_scale_feature(self):
        """Test scale the feature from Matlab original code."""
        brisque = BRISQUE()
        scaled_feat = brisque._scale_feature(self._brisque_feat)
        np.testing.assert_array_almost_equal(scaled_feat, self._scaled_feat)

    def test_get_feature(self):
        """The feature generated is equal up to 2 decimal points."""
        brisque = BRISQUE()
        image = cv2.imread(self._distorted_path, 0)
        feature = brisque.get_feature(image)
        np.testing.assert_array_almost_equal(
            feature, self._brisque_feat, decimal=2)
