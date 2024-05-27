#!/usr/bin/env python3
"""
Module: Tests for the utils module.
This module contains unit tests for the
functions defined in the utils module.
"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        Tests access_nested_map's output and
        handles exceptions.
        """
        try:
            result = access_nested_map(nested_map, path)
            self.assertEqual(result, expected)
        except KeyError as e:
            self.fail(f"Accessing nested map failed: {e}")

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """
        Tests access_nested_map's exception raising.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """
        Tests get_json's output and handles exceptions.
        """
        try:
            attrs = {'json.return_value': test_payload}
            with patch("requests.get", return_value=Mock(**attrs)) as req_get:
                result = get_json(test_url)
                self.assertEqual(result, test_payload)
                req_get.assert_called_once_with(test_url)
        except Exception as e:
            self.fail(f"Getting JSON failed: {e}")


class TestMemoize(unittest.TestCase):
    """
    Tests the memoize function.
    """

    def test_memoize(self) -> None:
        """
        Tests memoize's output and handles exceptions.
        """
        try:
            class TestClass:
                def a_method(self):
                    return 42

                @memoize
                def a_property(self):
                    return self.a_method()
            with patch.object(
                    TestClass,
                    "a_method",
                    return_value=lambda: 42,
                    ) as memo_fxn:
                test_class = TestClass()
                result1 = test_class.a_property()
                result2 = test_class.a_property()
                self.assertEqual(result1, 42)
                self.assertEqual(result2, 42)
                memo_fxn.assert_called_once()
        except Exception as e:
            self.fail(f"Memoization failed: {e}")
