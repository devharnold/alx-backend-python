#!/usr/bin/env python3
"""unittest module"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch
from unittest.mock import MagicMock
from typing import Dict, Tuple, Union


from utils import (access_nested_map, get_json, memoize)

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
    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get) -> None:
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test memoize function"""
    def test_memoize(self) -> None:
        """to test the output of the memoize function"""
        class TestClass:
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method
            
        with patch.object(TestClass, "a_method", return_value=42) as memoize_func:
            test_class = TestClass()
            self.assertEqual(test_class.a_proprty(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memoize_func.assert_called_once()