import pandas as pd
import re

#Open Apache.log file as read.
with open('log-files/Apache.log', 'r') as file:
    lines = file.readlines()

df = pd.DataFrame(lines)
line  = df.loc[0,0]

regex_pattern = r'\[(?P<datetime>[^\]]+)\]'
parsed_line = [re.match(regex_pattern, line).groupdict()]

print(parsed_line[0]['datetime'])


#for line in lines:
#    if re.match(regex_pattern, line):
#        parsed_data = re.match(regex_pattern, line)
#line_datetime = re.match("+\w +\w +\d +\d:\d\d:\d\d +\d", line)

#print(line)
