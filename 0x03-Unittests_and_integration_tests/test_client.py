#!/usr/bin/env python3
"""
Module: Tests for the client module.
This module contains unit tests for the GithubOrgClient class
defined in the client module.
"""

import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """
        Tests the org method and handles exceptions.
        """
        try:
            mocked_fxn.return_value = MagicMock(return_value=resp)
            gh_org_client = GithubOrgClient(org)
            result = gh_org_client.org()
            self.assertEqual(result, resp)
            mocked_fxn.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org)
            )
        except Exception as e:
            self.fail(f"Org test failed: {e}")

    def test_public_repos_url(self) -> None:
        """
        Tests the _public_repos_url property and handles exceptions.
        """
        try:
            with patch(
                    "client.GithubOrgClient.org",
                    new_callable=PropertyMock,
                    ) as mock_org:
                mock_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos",
                }
                result = GithubOrgClient("google")._public_repos_url
                self.assertEqual(
                    result,
                    "https://api.github.com/users/google/repos",
                )
        except Exception as e:
            self.fail(f"Public repos URL test failed: {e}")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Tests the public_repos method and handles exceptions.
        """
        try:
            test_payload = {
                'repos_url': "https://api.github.com/users/google/repos",
                'repos': [
                    {
                        "id": 7697149,
                        "name": "episodes.dart",
                        "private": False,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                        },
                        "fork": False,
                        "url": "https://api.github.com/repos/google/",
                        "episodes.dart",
                        "created_at": "2013-01-19T00:31:37Z",
                        "updated_at": "2019-09-23T11:53:58Z",
                        "has_issues": True,
                        "forks": 22,
                        "default_branch": "master",
                    },
                    {
                        "id": 8566972,
                        "name": "kratu",
                        "private": False,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                        },
                        "fork": False,
                        "url": "https://api.github.com/repos/google/kratu",
                        "created_at": "2013-03-04T22:52:33Z",
                        "updated_at": "2019-11-15T22:22:16Z",
                        "has_issues": True,
                        "forks": 32,
                        "default_branch": "master",
                    },
                ]
            }
            mock_get_json.return_value = test_payload["repos"]
            with patch(
                    "client.GithubOrgClient._public_repos_url",
                    new_callable=PropertyMock,
                    ) as mock_public_repos_url:
                mock_public_repos_url.return_value = test_payload["repos_url"]
                result = GithubOrgClient("google").public_repos()
                self.assertEqual(
                    result,
                    [
                        "episodes.dart",
                        "kratu",
                    ],
                )
                mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()
        except Exception as e:
            self.fail(f"Public repos test failed: {e}")

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Tests the has_license method and handles exceptions.
        """
        try:
            gh_org_client = GithubOrgClient("google")
            client_has_licence = gh_org_client.has_license(repo, key)
            self.assertEqual(client_has_licence, expected)
        except Exception as e:
            self.fail(f"Has license test failed: {e}")


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Performs integration tests for the `GithubOrgClient` class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Sets up class fixtures before running tests.
        """
        try:
            route_payload = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload,
            }

            def get_payload(url):
                if url in route_payload:
                    return Mock(**{'json.return_value': route_payload[url]})
                return HTTPError

            cls.get_patcher = patch("requests.get", side_effect=get_payload)
            cls.get_patcher.start()
        except Exception as e:
            raise RuntimeError(f"Setup class failed: {e}")

    def test_public_repos(self) -> None:
        """
        Tests the public_repos method and handles exceptions.
        """
        try:
            result = GithubOrgClient("google").public_repos()
            self.assertEqual(result, self.expected_repos)
        except Exception as e:
            self.fail(f"Public repos test failed: {e}")

    def test_public_repos_with_license(self) -> None:
        """
        Tests the public_repos method with a license and handles exceptions.
        """
        try:
            # result = GithubOrgClient("google").
            # public_repos(license="apache-2.0")
            client = GithubOrgClient("google")
            result = client.public_repos(license="apache-2.0")

            self.assertEqual(result, self.apache2_repos)
        except Exception as e:
            self.fail(f"Public repos with license test failed: {e}")

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Removes the class fixtures after running all tests.
        """
        try:
            cls.get_patcher.stop()
        except Exception as e:
            raise RuntimeError(f"Tear down class failed: {e}")
