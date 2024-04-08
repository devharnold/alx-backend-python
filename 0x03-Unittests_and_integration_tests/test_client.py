#!/usr/bin/env python3
"""Test client module"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch
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
    