import gspread

from local_settings import onetimepass, username

gc = gspread.login(username, onetimepass)


wks = gc.open("evaluation_NYT_2014_01 (Responses)").sheet1

# read every populated row in the spread sheet
def read_responses(sht):
    row = 2
    out = []

    while(len(sht.cell(row,1).value) > 0):
        vals = sht.row_values(row)
        out.append(vals)
        row += 1

    return out

