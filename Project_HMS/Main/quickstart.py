from __future__ import print_function

from googleapiclient.discovery import build


from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1_Y8qvIldHszD2JuZpqvVEcZMxqtofPMdrMm47iltA6o'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1").execute()
values = result.get('values', [])

aoa = [["heelo", "hi"],["heelo", "hi"]]


request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1",valueInputOption="USER_ENTERED", body={"values":aoa}).execute()

print(result)