#!/usr/env/env python3

"""Testing Client :
- client.GithubOrgClient 
- _public_repos_url 
- has_license
"""

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        """Test org"""
        test_url = "https://api.github.com/orgs/" + org
        test_payload = {"payload": True}
        with patch("client.get_json") as MockClass:
            MockClass.return_value = test_payload
            self.assertEqual(GithubOrgClient(org).org, test_payload)
            MockClass.assert_called_once_with(test_url)
