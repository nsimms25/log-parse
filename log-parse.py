import pandas as pd
import re

#Open Apache.log file as read.
with open('log-files/Apache.log', 'r') as file:
    lines = file.readlines()

#Regex pattern to get only entries with client information. Thanks regex101.com!
regex_pattern = r'\[(?P<datetime>[^\]]+)\] \[(?P<type>\S+)\] \[client (?P<client>\S+)\] (?P<reason>\D+): (?P<what>\S+)\n'

#Apply re pattern to lines if the regex exists, group as a dict and store in list for df creation later.
parsed_lines = [re.match(regex_pattern, line).groupdict() for line in lines if re.match(regex_pattern, line)]

#List above to DataFrame.
df = pd.DataFrame(parsed_lines)

#print(df.head())
#print(df[df.type == 'error'])

client_df = df.drop(columns=["datetime"])
client_df = client_df.groupby(["client", "what", "reason"]).count()

print(client_df.head())
