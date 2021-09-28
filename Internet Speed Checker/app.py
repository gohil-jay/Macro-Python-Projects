"""
!pip install speedtest-cli
"""

import speedtest

temp = speedtest.Speedtest()

print("Your download speed is : ", temp.download()//10**6, "MBPS")
print("Your upload speed is : ", temp.upload()//10**6, "MBPS")
