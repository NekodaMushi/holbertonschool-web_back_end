#!/usr/bin/env python3

"""UNITEST FOR THE WIN"""

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class testing access_nested_map fn"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            (
                {},
                ("a",),
                "a",
            ),
            ({"a": 1}, ("a", "b"), 1),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(context.exception, expected)


class TestGetJson(unittest.TestCase):
    """Test Json Fn"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        with patch("requests.get") as mock_method:
            mock_method.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_method.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class test memoize"""

    def test_memoize(self):
        """Fn test memoize"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked:
            obj = TestClass()
            obj.a_property
            obj.a_property
            mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()
