# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from checkedid.api.authentication_api import AuthenticationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from checkedid.api.authentication_api import AuthenticationApi
from checkedid.api.invitation_api import InvitationApi
from checkedid.api.report_data_api import ReportDataApi
from checkedid.api.status_api import StatusApi
from checkedid.api.users_api import UsersApi
