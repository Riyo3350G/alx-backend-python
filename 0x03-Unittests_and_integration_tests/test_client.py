#!/usr/bin/env python3
"""Client Test Module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
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
            f"https://api.github.com/orgs/{name_org}"
        )
