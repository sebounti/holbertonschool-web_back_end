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
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("openai")
        self.assertEqual(client.has_license(repo, license_key), expected)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                        'apache2_repos'),
                        TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.get_json')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def setUp(self):
        self.get_patcher = patch('client.get_json')
        self.mock_get = self.get_patcher.start()

    def tearDown(self):
        self.get_patcher.stop()

    def test_public_repos(self):
        self.mock_get.side_effect = [self.org_payload, self.repos_payload]
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.mock_get.assert_called_with(test_class._public_repos_url)

    def test_public_repos_with_license(self):
        self.mock_get.side_effect = [self.org_payload, self.repos_payload]
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos('apache-2.0'), self.apache2_repos)
        self.mock_get.assert_called_with(test_class._public_repos_url)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()
