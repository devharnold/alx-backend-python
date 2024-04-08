#!/usr/bin/env python3
"""unittest module"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
from unittest.mock import Mock, patch
from unittest.mock import MagicMock

class TestAccessNestedMap(unittest.TestCase):
    """access nested map module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

class TestAccessNestedMap(unittest.TestCase):
    """access nested map execution module"""
    def test_access_nested_map_execution(self, nested_map, path, expected_result):
        nested_map = {"a": {"b": {"c": 1}}}
        try:
            with self.assertRaises(KeyError):
                access_nested_map(nested_map, ["a", "x", "z"])
        except KeyError as e:
            with self.assertRaises(KeyError):
                access_nested_map({"a": 1}, ["a", "b", "c"])
            self.assertEqual(e.exception.message, 'error message')

class TestGetJson(unittest.TestCase):
