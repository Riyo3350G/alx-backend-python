#!/usr/bin/env python3
"""Client Test Module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, name_org, mock_get: MagicMock):
        """Test org"""
        test_class = GithubOrgClient(name_org)
        test_class.org()
        mock_get.assert_called_once_with(
            test_class.ORG_URL.format(org=name_org)
        )

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get: MagicMock):
        """Test public repos url"""
        test_class = GithubOrgClient("google")
        test_class.org()
        self.assertEqual(
            test_class._public_repos_url,
            mock_get.return_value["repos_url"]
        )

    @patch('client.get_json')
    def test_public_repos(self, mock_get: MagicMock):
        """Test public repos"""
        test_class = GithubOrgClient("google")
        test_class.org()
        test_class.repos_payload()
        self.assertEqual(
            test_class.public_repos(),
            [repo["name"] for repo in mock_get.return_value]
        )
