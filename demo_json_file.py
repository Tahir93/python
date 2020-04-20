import json

alphabet_letter = ["a", "b", "c", "f"]
dictionary_data = {"name":"Ali", "age":32, "gender":"M"}


with open("demo_json_file.json", "w") as file:
    json.dump(dictionary_data, file)

with open("demo_json_file.json", "r") as file:
    content = json.load(file)

print(content)

