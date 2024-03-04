#!/usr/bin/env python3
"""
file unittests
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, data, mocked_get_json):
        ''' test org'''
        endpoint = f'https://api.github.com/orgs/{data}'
        test_class = GithubOrgClient(data)
        test_class.org()
        mocked_get_json.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url
        is the expected one based on the mocked payload."""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock) as patched:
            test_json = {"url": "linkedin",
                         "repos_url": "http://google.com"}
            patched.return_value = test_json
            github_client = GithubOrgClient(test_json.get("url"))
            response = github_client._public_repos_url
            patched.assert_called_once()
            self.assertEqual(response, test_json.get("repos_url"))
