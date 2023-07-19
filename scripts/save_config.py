import json
import sys
 
config_file = sys.argv[1]
dictionary = {}

for index,item in enumerate(sys.argv):
    if index < 2:
        continue
    if index % 2 != 0:
        dictionary[sys.argv[index-1]] = sys.argv[index].replace("\\", "/")

#print(dictionary)
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open(config_file, "w") as outfile:
    outfile.write(json_object)