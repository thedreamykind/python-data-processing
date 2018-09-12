from pprint import pprint
import json
import csv

# Phase 1 - Process the readings.
# Sample reading - {"date": "20180315", "user": {"id": "2708"}, "temperature": 98.2}

# Store the ids of users with a fever in a set (for uniqueness). 
unique_user_ids_with_fever = set()

with open('readings.jsonl') as jsonl_file:
	# For each reading in readings.jsonl,
	for line in jsonl_file:
		reading = json.loads(line)
		# if the temperature reading indicates a fever,
		if (reading["temperature"] > 99.5):
			# store the user_id in a set. 
			unique_user_ids_with_fever.add(reading["user"]["id"])

# Phase 2 - Generate the output.
# Sample user - 2054,99178,Darin Darden

# Dictionary - {key = zip, value = number of unique people with a fever}
zip_fever_count = dict()

with open('user_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # For each user in user_data.csv,
    for user in csv_reader:
    	user_id = user[0]
    	user_zip = user[1]
    	# if the user has a fever,
    	if user_id in unique_user_ids_with_fever:
    		# update the dictionary. 
    		if user_zip in zip_fever_count:
    			zip_fever_count[user_zip] = (zip_fever_count[user_zip] + 1)
    		else:
    			zip_fever_count[user_zip] = 1

print "Debug output format - {key = zip, value = number of unique people with a fever}"
pprint(zip_fever_count)

# Write the results to a csv file. 
with open('fever_count_by_zip.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["zip","unique_fever_count"])
    for key, value in zip_fever_count.items():
       writer.writerow([key, value])
