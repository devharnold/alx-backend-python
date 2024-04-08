#!/usr/bin/env python3
"""unittest module"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """access nested map module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)