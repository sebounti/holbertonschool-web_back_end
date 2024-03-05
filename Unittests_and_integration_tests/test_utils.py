#!/usr/bin/env python3
"""
file unittests
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from typing import Any, Dict, List, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """ Access nested map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[Any, Any],
                               path: List[str], expected: Any) -> None:
        """ Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[Any, Any],
                                         path: List[str]):
        ''' test exception'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' get json unittest '''
    #  teste la fonction get_json avec différents paramètres.
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        ''' self descriptive'''
        # Classe interne Mocked pour simuler la réponse d'une requête HTTP.
        class Mocked(Mock):
            ''' mocked class'''

            def json(self):
                ''' json method mocked'''
                return test_payload

        # Utili patch pour remplacer l'appel à requests.get par un objet mock.
        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class Testmemoize(unittest.TestCase):
    """ memoize unittest """

    def test_memoize(self):
        """ self descriptive """

        # Définition d'une classe test pour illustrer l'usage de memoize.
        class TestClass:
            """ test class """
            def a_method(self):
                """ a method """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            first = test.a_property
            second = test.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
