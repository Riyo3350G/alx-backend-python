#!/usr/bin/env python3
"""Client Test Module"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock, Mock
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

    @parameterized.expand([
       ({"license": {"key": "my_license"}}, "my_license", True),
       ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )

    @parameterized_class((
        "org_payload",
        "repos_payload",
        "expected_repos",
        "apache2_repos"),
        TEST_PAYLOAD)
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """TestIntegrationGithubOrgClient Class"""
        @classmethod
        def setUpClass(cls):
            """Set up class"""
            def effect(url):
                """side effect"""
                rp = []
                mock = Mock()
                for payload in TEST_PAYLOAD:
                    if url == payload[0]["repos_url"]:
                        rp = payload[1]
                        break
                mock.json.return_value = rp
                return mock
            cls.get_patcher = patch('requests.get', side_effect=effect)
            cls.org_patcher = patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock,
                return_value=cls.org_payload
            )
            cls.get_patcher.start()
            cls.org_patcher.start()

        @classmethod
        def tearDownClass(cls):
            """Tear down class"""
            cls.get_patcher.stop()
            cls.org_patcher.stop()

        def test_public_repos(self):
            """Test public repos"""
            test_class = GithubOrgClient("google/repos")
            self.assertEqual(
                test_class.public_repos(),
                self.expected_repos
            )

        def test_public_repos_with_license(self):
            """Test public repos with license"""
            test_class = GithubOrgClient("google/repos")
            self.assertEqual(
                test_class.public_repos("apache-2.0"),
                self.apache2_repos
            )
