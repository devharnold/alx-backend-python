#!/usr/bin/env python3
"""Test client module"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import mock, patch, PropertyMock, patch
from unittest.mock import MagicMock
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test githuborg class"""
    @parameterized.expand([
        ("google", {'login' "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json",)
    def test_org(self, org: str, repo: Dict, mocked_fn: MagicMock) -> None:
        """tests the get_org method"""
        mocked_fn.return_value = MagicMock(return_value=repo)
        g_org_client = GithubOrgClient(org)
        self.assertEqual(g_org_client.org(), repo)
        mocked_fn.assert_called_once_with("https://api.github.com/orgs/{}".format(org))
    
    #@mock.patch('GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos_url(self) -> str:
        """testing the `_public_repos_url` property"""
        with patch("GithubClient.org", new_callable=PropertyMock,) as mock_org:
            mock_org.return_value = {'repos_url': "https://api.github.com/users/google/repos",}
            self.assertEqual(GithubOrgClient("google")._public_repos_url, "https://api.github.com/users/google/repos",)

    @patch("get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """tests the `public repos`."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                          {
        "id": 7697149,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
      },
      {
        "id": 7776515,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
        "name": "cpp-netlib",
        "full_name": "google/cpp-netlib",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
      },
                }
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "GithubOrgClient._public_repos_url", new_callable=PropertyMock, 
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(GithubOrgClient("google".public_repos(), ["episodes.dart", "cpp-netlib"]))
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


    @parameterized.expand([
        ({'license': {'key': ""}}, "", True),
        ({'license': {'key': ""}}, "", False),
    ])
    def test_has_licese(self, repo: Dict, key: str, expected: bool) -> None:
        """tests has_license"""
        g_org_client = GithubOrgClient("google")
        client_has_license = g_org_client.has_license(repo, key)
        self.assertEqual(client_has_license, expected)
