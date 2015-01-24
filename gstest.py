import gspread

from local_settings import onetimepass, username

gc = gspread.login(username, onetimepass)


wks = gc.open("evaluation_NYT_2014_01 (Responses)").sheet1

# read every populated row in the spread sheet
def read_responses(sht):
    row = 2
    out = []
    fields = ['timestamp', 'quantitative rating', 'qualitative rating', 'keywords / tags', 'optional keywords', 'endorsement', 'username']

    # iterate through rows until cell 1 is empty
    while(len(sht.cell(row,1).value) > 0):
        vals = sht.row_values(row)
        row_data = {}
        for i in range(len(vals)):
            row_data[fields[i]] = vals[i]

        out.append(row_data)
        row += 1

    return out

def auto_read_responses():
    return read_responses(wks)
