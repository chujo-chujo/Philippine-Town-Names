import extract_cities
from towns import dict_of_town_names

#############################################

grfid    = "CH\\12\\01"
version  = "1"
min_comp = "1"
output   = "philippine_town_names.nml"

#############################################

header = """grf {
    grfid: \"""" + grfid + """\";
    name: string(STR_GRF_NAME);
    desc: string(STR_GRF_DESC);
    url: string(STR_GRF_URL);
    version: """ + version + """;
    min_compatible_version: """ + min_comp + """;
}

town_names(philippine_town_names) {
    {
"""

footer = """
    }
}

town_names {
    styles: string(STR_OPTIONS);
    {
        town_names(philippine_town_names, 1)
    }
}
"""

def create_nml_line(data):
    # data => a tuple of name and population
    name = data[0]
    pop  = data[1]
    probability = 1
    # Adjust probabilities based on population
    if pop >= 1500000:
        probability = 60
    elif pop > 500000:
        probability = 25
    elif pop > 70000:
        probability = 6
    elif pop > 35000:
        probability = 3

    if name == list(sorted_dict_of_town_names.keys())[-1]:
        return "        text(\"" + name + "\", " + str(probability) + ")"
    else:
        return "        text(\"" + name + "\", " + str(probability) + "),\n"

# Sort "dict_of_town_names" by population in descending order
sorted_dict_of_town_names = dict(sorted(dict_of_town_names.items(), key=lambda item: item[1], reverse=True))

nml_lines = [create_nml_line(data) for data in list(sorted_dict_of_town_names.items())]
with open(output, mode='w') as output_file:
    output_file.write(header + ''.join(nml_lines) + footer)