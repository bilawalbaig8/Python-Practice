def openFile(filename):
    file=open(filename,'r')
    data=file.read()
    return data
def appendHeader(filename):
    file = open(filename, 'a')
    header="PatientId"+"\t"+"Name"+"\t"+"Contact"+"\t"+"Address"+"\t"+"BOD"+"\t"+"Gender"+"\t"+"AppDates"+"\t"+"Medicines"+"\t"+"Remarks"
    file.write(header)

def appendRecord(filename,data):
    file=open(filename,'a')
    file.write("\n")
    file.write(data)
    return data

def readAllRecords(filename):
    file=open(filename,'r')
    rows=file.readlines()
    return rows

def writenewfile(filename,data):
    file = open(filename, 'w')
    w = file.write(data)
    return w
