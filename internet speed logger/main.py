import speedtest
from sql import SQL
import time
import matplotlib.pyplot as plt

st = speedtest.Speedtest()
DB = SQL("database")
sm = 2629800
sd = 86400
# sd = 350
option = int(input('''What speed do you want to test:  
  
1) scan  
  
2) review daily  
  
3) review monthly 
  
Your Choice: '''))

if option == 1:

    upS = st.download()/1000000
    downS = st.upload()/1000000
    servernames = []
    st.get_servers(servernames)
    pingS = st.results.ping

    timeS = time.time()

    DB.SqlAddDet(upS, downS, pingS, timeS)
elif option == 2:
    records = DB.QuaryRecordMaster()
    lr = (records[-1])[3]
    check = 0
    sumD = []
    sumDtemp = 0
    sumU = []
    sumUtemp = 0
    sumP = []
    sumPtemp = 0
    i = 0
    while check != 1:
        check = 1
        for r in records:
            if lr > r[3]:
                check = 0
            
            if lr-r[3] < sd:
                sumUtemp += r[0]
                sumDtemp += r[1]
                sumPtemp += r[2]
                i += 1
        if check == 0:
            sumUtemp /= i
            sumDtemp /= i
            sumPtemp /= i
            sumU.append(sumUtemp)
            sumD.append(sumDtemp)
            sumP.append(sumPtemp)
            sumUtemp = 0
            sumDtemp = 0
            sumPtemp = 0
            i = 0
            lr = lr-sd
    plt.scatter(sumD, range(len(sumD)))
    plt.scatter(sumU, range(len(sumD)))
    plt.scatter(sumP, range(len(sumD)))
    plt.legend(["download", "upload", "ping"])
    plt.show()

elif option == 3:
    records = DB.QuaryRecordMaster()
    lr = (records[-1])[3]
    check = 0
    sumD = []
    sumDtemp = 0
    sumU = []
    sumUtemp = 0
    sumP = []
    sumPtemp = 0
    i = 0
    while check != 1:
        check = 1
        for r in records:
            if lr > r[3]:
                check = 0
            
            if lr-r[3] < sm:
                sumUtemp += r[0]
                sumDtemp += r[1]
                sumPtemp += r[2]
                i += 1
        if check == 0:
            sumUtemp /= i
            sumDtemp /= i
            sumPtemp /= i
            sumU.append(sumUtemp)
            sumD.append(sumDtemp)
            sumP.append(sumPtemp)
            sumUtemp = 0
            sumDtemp = 0
            sumPtemp = 0
            i = 0
            lr = lr-sm
    plt.scatter(sumD, range(len(sumD)))
    plt.scatter(sumU, range(len(sumD)))
    plt.scatter(sumP, range(len(sumD)))
    plt.legend(["download", "upload", "ping"])
    plt.show()
