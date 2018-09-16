import csv
import os
from common.tool import getRootDir

rootdir = getRootDir()
logindata_csv = os.path.join(rootdir ,'data','login_data.csv')

def parse_csv():
    arr=[]
    with open(logindata_csv,encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            arr.append(row)
    return arr

