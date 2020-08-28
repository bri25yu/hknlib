from __future__ import unicode_literals

SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.group.member',
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/gmail.send'
]

# Stores API key
SERVICE_ACCOUNT_FILE = 'secret/service.json'

# Elections spreadsheet
SPREADSHEET_ID = '1wnZfinKlVUsdXaz-W0ACnb_G7HFfDVlpudUSGpA1GrM'

NEW_OFFICER_SHEET = 'New Officers Fa20'
# OLD_OFFICER_SHEET = 'Returning Officers'
MEMBER_SHEET = 'New Members Fa20'

NEW_OFFICER_SHEET_ID = '86797048'
# OLD_OFFICER_SHEET_ID = '682750401'
MEMBER_SHEET_ID = '422415673'

NEW_OFFICER_RANGE = '\'{}\'!A:G'.format(NEW_OFFICER_SHEET)
#OLD_OFFICER_RANGE = '\'{}\'!A:F'.format(OLD_OFFICER_SHEET)
MEMBER_RANGE = '\'{}\'!A:F'.format(MEMBER_SHEET)
