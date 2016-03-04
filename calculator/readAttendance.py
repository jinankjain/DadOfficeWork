import csv
import sys
from datetime import datetime

def readAttendance(fileName):
    
    f = open(fileName, 'rt')
    try:
        reader = csv.DictReader(f)
        salary = {}
        for row in reader:
            temp = row['Punch Records '].split()
            
            totalSeconds = 0
            
            inTime = ""
            outTime = ""
            for t in temp:
                t1 = t.split(":")
                t2 = t1[2].split("(")
                if t2[0]=="in":
                    s = str(t1[0])+":"+str(t1[1])
                    inTime = datetime.strptime(s,'%H:%M')
                if t2[0]=="out":
                    s = str(t1[0])+":"+str(t1[1])
                    outTime = datetime.strptime(s,'%H:%M')
    
                if outTime and inTime:
                    delta = (outTime - inTime)
                    totalSeconds+=delta.seconds
                    inTime = ""
                    outTime = ""
            if inTime and outTime=="":
                print row['Employee Name'] + " Forgot to do outTime"
            salary.update({str(row[' Employee Code ']): ((totalSeconds)/60)/(1.0*60)})
            print ((totalSeconds)/60)/(1.0*60)
        return row['Date'], salary
    finally:
        f.close()
