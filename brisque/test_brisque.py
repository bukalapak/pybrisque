# coding=utf-8
import unittest

import numpy as np
import cv2

from brisque import BRISQUE
from brisque.utilities import root_path


class TestBRISQUE(unittest.TestCase):
    def setUp(self):
        self._paths = [
            root_path('examples','i04_14_1.bmp'),
            root_path('examples', 'bl_image.jpg')]

        # These feature are extracted from the original Matlab code of the
        # distorted image above (
        # https://github.com/dsoellinger/blind_image_quality_toolbox/tree/master/%2Bbrisque)
        self._brisque_feats = [
            np.array([
                2.187000, 0.305119, 0.731000, 0.046159, 0.078954, 0.124348,
                0.735000, 0.032419, 0.086307, 0.118338, 0.733000, -0.020298,
                0.112611, 0.092477, 0.730000, -0.022557, 0.114732, 0.092231,
                2.103000, 0.360946, 0.731000, -0.055774, 0.183185, 0.116578,
                0.734000, -0.046589, 0.179101, 0.123198, 0.730000, -0.037948,
                0.168773, 0.123828, 0.725000, -0.033253, 0.165621, 0.126170
        ]), np.array([
                0.4610000, 0.1652788, 0.3410000, -0.1192659,  0.2319912,
                0.0417499, 0.3370000, -0.1010206, 0.2127568, 0.0502738,
                0.3410000, -0.1070136, 0.1971343, 0.0380880, 0.3390000,
                -0.0978340, 0.1865236, 0.0413579, 0.4860000, 0.1888571,
                0.3480000, -0.0518405, 0.1354198, 0.0621431, 0.3500000,
                -0.0487347, 0.1329318, 0.0642503, 0.3420000, -0.0046308,
                0.0917469, 0.0853537, 0.3410000, -0.0035089, 0.0918414,
                0.0869626
            ])
        ]
        self._scaled_feats = [
            np.array([
                -0.617264, -0.270555, -0.295875, 0.0406103, -0.778699, -0.474667,
                -0.297065, 0.0308621, -0.757414, -0.500593, -0.258806,
                -0.0243801, -0.671236, -0.656588, -0.275518, -0.00898751,
                -0.665791, -0.658926, 0.168636, 0.00856362, 0.23913, -0.72301,
                -0.171255, -0.433049, 0.24878, -0.502953, -0.193939, -0.392484,
                0.308192, -0.264632, -0.365476, -0.333965, 0.304462, -0.19329,
                -0.375196, -0.322727]),
            np.array([
                -0.974539, -0.624845, -0.85064, -0.971739, -0.348906,
                -0.826796, -0.866858, -0.850893, -0.401369, -0.790221,
                -0.859112, -0.757568, -0.424093, -0.860575, -0.875672,
                -0.62628, -0.456337, -0.848885, -0.989259, -0.489984,
                -0.68599, -0.695149, -0.387366, -0.700702, -0.687805,
                -0.518371, -0.401745, -0.686448, -0.70091, 0.0445592,
                -0.655117, -0.542798, -0.703412, 0.0757798, -0.653578,
                -0.535069]),
        ]
        # The expected score from Matlab
        self._expected_score = [52.521, 123.74]

        # Our score
        self._score = [50.2686, 122.8447]

    def test_from_path(self):
        """Test directly from the path."""
        brisque = BRISQUE()
        for idx, path in enumerate(self._paths):
            self.assertAlmostEqual(
                brisque.get_score(path), self._score[idx], places=3)

    def test_from_grayscale(self):
        brisque = BRISQUE()
        for idx, path in enumerate(self._paths):
            image = cv2.imread(path, 0)
            self.assertAlmostEqual(
                brisque.get_score(image), self._score[idx], places=3)

    def test_score_from_scaled_feature(self):
        """Test score from scaled feature from Matlab original code."""
        brisque = BRISQUE()
        for idx, scaled_feat in enumerate(self._scaled_feats):
            score = brisque._calculate_score(scaled_feat)
            self.assertAlmostEqual(score, self._expected_score[idx], places=2)

    def test_scale_feature(self):
        """Test scale the feature from Matlab original code."""
        brisque = BRISQUE()
        for idx, feat in enumerate(self._brisque_feats):
            scaled_feat = brisque._scale_feature(feat)
            np.testing.assert_array_almost_equal(
                scaled_feat, self._scaled_feats[idx], decimal=5)

    def test_get_feature(self):
        """The feature generated is equal."""
        brisque = BRISQUE()
        for idx, path in enumerate(self._paths):
            image = cv2.imread(path, 0)
            feature = brisque.get_feature(image)
            np.testing.assert_array_almost_equal(
                feature, self._brisque_feats[idx], decimal=0)
        # brisque = BRISQUE()
        # image = cv2.imread('/home/akbar/dev/ml/pybrisque/examples/bl_image.jpg')
        # feature = brisque.get_feature(image)
