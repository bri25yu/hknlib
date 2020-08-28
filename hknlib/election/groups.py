from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from googleapiclient.discovery import build
from .settings import SPREADSHEET_ID


def add_user_to_group(credentials, user, groupKey):
    #add USER to a mail list GROUP
    service = build('admin', 'directory_v1', credentials=credentials)

    body = {
        'email': user + '@hkn.eecs.berkeley.edu',
        'role': 'MEMBER',
    }
    group = groupKey + '@hkn.eecs.berkeley.edu'
    response = service.members().hasMember(groupKey=group, memberKey=body.get('email')).execute()
    if response['isMember']:
        return
    _ = service.members().insert(groupKey=group, body=body).execute()
    print("{}->{}".format(user, groupKey))
    return


def add_officers_to_committes(credentials, election_data):
    user_committee = []
    if election_data:
        for signup in election_data:
            if len(signup) < 6:
                continue
            committee_selection = signup[5] # e.g. compserv@ or N/A
            if committee_selection != 'N/A':
                committee = committee_selection[:-1]
                user = signup[3] # e.g. test_user
                user_committee.append((user, committee))
            #user_committee[users[i]] = committee

    for user, committee in user_committee:
        result = add_user_to_group(credentials, user, committee+'-officers')
        result = add_user_to_group(credentials, user, "current-"+committee)


def add_members_to_committes(credentials, election_data):
    mailing_lists = []
    if election_data:
        for i in range(0, len(election_data)):
            if len(election_data[i]) < 7:
                continue
            row = election_data[i]
            mailing = row[6][:-1].split('@, ')
            mailing_lists.append((election_data[i][3], mailing))
            #mailing_lists[users[i]] = mailing_list

    for user, mailing_list in mailing_lists:
        for committee in mailing_list:
            add_user_to_group(credentials, user, committee)

def add_all_to_committes(credentials, election_data):
    # add all users to their committees and groups
    add_officers_to_committes(credentials, election_data)
    add_members_to_committes(credentials, election_data)
