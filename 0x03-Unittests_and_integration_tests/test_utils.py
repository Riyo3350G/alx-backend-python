#!/usr/bin/env python3
"""Utils Test Module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self):
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map({"a": 1}, ("b",))
