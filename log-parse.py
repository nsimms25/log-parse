import pandas as pd
import re

#Open Apache.log file as read.
with open('log-files/Apache.log', 'r') as file:
    lines = file.readlines()

regex_pattern = r'\[(?P<datetime>[^\]]+)\] \[(?P<type>\S+)\] \[client (?P<client>\S+)\] (?P<reason>\D+): \D+\n'
parsed_lines = [re.match(regex_pattern, line).groupdict() for line in lines if re.match(regex_pattern, line)]

df = pd.DataFrame(parsed_lines)

print(df.head())
print(df[df.type == 'error'])
