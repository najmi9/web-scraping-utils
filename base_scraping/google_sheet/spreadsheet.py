import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sheet(sheet_name = "spread_sheet_name",credentials_file='credentials.json', scope = []):
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
	client = gspread.authorize(creds)
	try:
		sheet = client.open(sheet_name).sheet1
		return sheet
	except Exception as e:
		print(e)

sheet(sheet_name = "Python", credentials_file='credentials.json', scope=[])
"""
	api:
		sheet:
			get_all_values() => [[], [], []] # get all rows
			get('A1') =>[[value]] # get a value of a cell
			update('A1', 'content') # update a cell
			insert_row([values], index) # insert a row
			delete_row(index) # delete a row with index
			row_count() #  get the number od rows
			find(query, in_row=None, in_column=None)
# steps : 
#  1 - create a new project 
#  2 -enable google drive api
#  3- enable sheet api
#  4- create credentials
#  5- save the credentials file
"""