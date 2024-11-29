import csv
import pprint

input_file  = "worldcities.csv"
output_csv  = "worldcities-Philippines.csv"
output_dict = "towns.py"
processed   = set()
dict_of_town_names = dict()

def add_to_dict(data):
	dict_of_town_names[data[0]] = int(data[1])

with open(input_file, mode="r", encoding="utf-8") as infile, \
	 open(output_csv, mode="w", encoding="utf-8", newline="") as outfile:
	
	reader = csv.reader(infile, delimiter=",")
	writer = csv.writer(outfile, delimiter=",")

	def add_city(data):
		if data[0] not in processed:
			writer.writerow(data)
			processed.add(data[0])
			add_to_dict(data)

	# Extract only Philippine cities, their ASCII names and population
	for row in reader:
		if len(row) >= 5 and row[4] == "Philippines":
			if row[1] == "Manila":
				manila_pop = int(row[9])//10
				add_city([row[1], str(manila_pop)])

			elif " City" in row[1] and row[1] != "Quezon City":
				city_name = row[1].replace(" City", "")
				add_city([city_name, row[9]])

			elif "Banco Filipino" in row[1]:
				continue

			else:
				add_city([row[1], row[9]])


prefix = f"# {len(processed)} Philippine cities (source: https://simplemaps.com/data/world-cities)\n\n"
formatted_dict = pprint.pformat(dict_of_town_names, indent=4)
with open(output_dict, "w") as file:
	file.write(prefix + "dict_of_town_names = {" + "\n " +  formatted_dict[1:])

print(f"Total number of names: {len(processed)}")