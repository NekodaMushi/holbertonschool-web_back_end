#!/usr/bin/env python3

"""Testing Client
"""

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
import client


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

    def test_public_repos_url(self):
        """Test public repos URL"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mc:
            mc.return_value = {"repos_url": "test.io"}
            org_client = client
            org_client = org_client.GithubOrgClient("test_org")
            self.assertEqual(org_client.org["repos_url"],
                             org_client._public_repos_url)

    @patch("client.get_json", return_value={})
    def test_public_repos(self, patched):
        """Test public repos"""
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            return_value=[],
        ) as mc:
            obj = GithubOrgClient("google")
            result = obj.public_repos(license="f")
            self.assertEqual(result, mc.return_value)
            patched.assert_called_once()
            mc.assert_called_once()
