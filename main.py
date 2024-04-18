import pandas as pd
import json

# Read JSON
with open('data.json') as inputfile:
  data = json.load(inputfile)

# Extract values
values_list = data.get('prefixes', [])

# Normalize nested values
df = pd.json_normalize(values_list)

# Extract desired fields
selected_columns = [
    'ip_prefix', 
    'region', 
    'service', 
    'network_border_group'
]
df_selected = df[selected_columns]

# Write DF to CSV
df.to_csv('IPv4_Ranges.csv', index=False)
print("Values have been added. Please check the output.csv file.")

# Secondary JSON -> CSV for IPv6 Prefix
with open('data.json') as inputfile:
  data = json.load(inputfile)

# Extract values
values_list = data.get('ipv6_prefixes', [])

# Normalize nested values
df = pd.json_normalize(values_list)

# Extract desired fields
selected_columns = [
    'ipv6_prefix', 
    'region', 
    'service', 
    'network_border_group'
]
df_selected = df[selected_columns]

# Write DF to CSV
df.to_csv('IPv6_Ranges.csv', index=False)
print("Values have been added. Please check the output.csv file.")
