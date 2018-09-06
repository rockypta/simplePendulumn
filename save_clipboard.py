import gspread
import sys
import getopt
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name("7c42eb356854.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("Clipboard").sheet1

column_toSet=1
last_row=int(wks.cell(1,2).value)
link_toSave = sys.argv[1]
last_row += 1
wks.update_cell(last_row,1,link_toSave)

Memos