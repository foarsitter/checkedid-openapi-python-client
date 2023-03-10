"""
    CheckedID API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import checkedid
from checkedid.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invitees_activate_employees(self):
        """Test case for invitees_activate_employees

        Activate Users  # noqa: E501
        """
        pass

    def test_invitees_create_employee(self):
        """Test case for invitees_create_employee

        Create Users  # noqa: E501
        """
        pass

    def test_invitees_delete_user(self):
        """Test case for invitees_delete_user

        Delete User  # noqa: E501
        """
        pass

    def test_invitees_update_employees(self):
        """Test case for invitees_update_employees

        Update Users  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
