#!/usr/bin/env python3
"""
file unittests
"""
import unittest
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
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
        """Test that the result of _public_repos_url"""
        with patch.object("client.GithubOrgClient.org",
                          new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Text more public repos """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_as_license(repo, license_key, expected):
        # Assuming GithubOrgClient is initialized with an organization name.
        client = GithubOrgClient("openai")
        assert client.has_license(repo, license_key) == expected
        assert client.has_license.__annotations__['return'] == bool
        assert client.has_license.__annotations__['repo'] == dict
        assert client.has_license.__annotations__['license_key'] == str
        assert client.has_license.__annotations__['expected'] == bool
