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


class TestGetJson(unittest.TestCase):
    """TestGetJson Class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json"""
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """TestMemoize Class"""
    def test_memoize(self):
        """Test memoize method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            result1 = test.a_property
            result2 = test.a_property
            mock.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
