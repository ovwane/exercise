from datetime import datetime

a = '2012-01-31 09:00:22'
b = '2012-01-31 10:00:22'
data1 = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
data2 = datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
data3 = datetime.strftime(data1, '%Y-%m-%dT%H:%M:%SZ')
print(data3)
if data1 < data2:
    print(1)