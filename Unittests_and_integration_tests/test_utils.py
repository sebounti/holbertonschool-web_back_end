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

        # Utilise patch pour remplacer l'appel à requests.get par un objet mock.
        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)

class Testmemoize(unittest.TestCase):
    ''' memoize unittest '''
    def test_memoize(self):
        ''' self descriptive'''
        # Définition d'une classe test pour illustrer l'usage de memoize.
        class TestClass:
            ''' test class'''
            def a_method(self):
                ''' a method'''
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Utilis de patch pour créer un mock de a_method dans TestClass.
        # Ceci permet de vérifier si la méthode est appelée plus d'une fois.
        with patch.object(TestClass, 'a_method') as mock:
            # Création d'une instance de TestClass pour le test.
            spec = TestClass()
            # Premier accès à la propriété a_property.
            # doit déclencher l'appel de a_method et mis en cache du résultat.
            spec.a_property
            # Deuxième accès à la même propriété.
            # Si fonctionne, a_method ne doit pas être appelée une seconde fois.
            spec.a_property
            # Vérification que a_method a été appelée une seule fois,
            # confirme ainsi que le résultat a été correctement mis en cache.
            mock.assert_called_once()

if __name__ == "__main__":
    unittest.main()
