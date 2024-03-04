#!/usr/bin/env python3
"""
file unittests
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
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
        """
        test access nested map

        Args:
        nested_map: dict
            nested map
        path: list
            list of keys
        result_expected: any
            expected value

        Returns:
            ok if test passes
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
