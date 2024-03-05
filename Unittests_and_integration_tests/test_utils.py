#!/usr/bin/env python3
"""Module for utils.py unittests"""
import json
from parameterized import parameterized
import requests
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """get_json unit tests"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that utils.get_json returns the expected result"""
        with patch('requests.get') as mock_request:
            mock_request().json.return_value = test_payload
            mock_request.assert_called_once()
            response = get_json(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """memoize unit test """

    def test_memoize(self):
        """Test that when calling a_property twice, the correct result is
        returned but a_method is only called once using assert_called_once"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            first = test.a_property
            second = test.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock.assert_called_once()
