import os
import pandas as pd
import csv

os.chdir("C:/Users/newsd/home/code/test_clean_events")

fips = pd.read_table("fips_codes.txt", delimiter = "|")
state_fips = fips["STATEFP"]
fips_list = state_fips.to_string()
fips_list = "","".join(map(str, fips_list))

lines = ""
current_line = ""
with open("example_lines.txt") as file:
    for line in file:
        previous_line = current_line
        current_line = line
        if not line.startswith("TT" or fips_list):
            new_line = previous_line + current_line
        else:
            new_line = current_line
    with open('test_output.csv', 'w') as output_file:
            writer = csv.writer(output_file, delimiter = "|")
            writer.writerows(new_line)


    
