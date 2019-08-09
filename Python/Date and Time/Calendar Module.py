# Enter your code here. Read input from STDIN. Print output to STDOUT
res = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
import datetime
pointer = list(map(int, input().split()))
print(res[datetime.date(pointer[2],pointer[0],pointer[1]).weekday()])
