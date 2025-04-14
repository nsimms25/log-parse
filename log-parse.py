import pandas as pd
import re

#Open Apache.log file as read.
with open('log-files/Apache.log', 'r') as file:
    lines = file.readlines()

df = pd.DataFrame(lines)

line  = df.loc[0,0]
#line_datetime = re.match("+\w +\w +\d +\d:\d\d:\d\d +\d", line)
line_datetime = re.match("\[\w\w\w \w\w\w \d\d \d\d\:\d\d\:\d\d \d\d\d\d\]", line)[0]

print(line_datetime)
#print(line)
