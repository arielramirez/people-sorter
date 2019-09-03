# Task:
#In the language of your choice, please write a function that takes in a list of unique people and returns a list of the people sorted. People have a name, age, and social security number. Their social security number is guaranteed to be unique. The people should be sorted by name (alphabetically) and age (oldest to youngest). When people have the same name and age, they should be sorted in reverse order of how they are in the original list. (When we say “list” you can interpret it as array, list, collection, etc.)
import json

#stub
def sort_people(raw_people):
	for person in raw_people:
		print(person["name"]) 
	return raw_people

with open('ep_4_people.json') as json_file:
	people_json = json.load(json_file)
	sort_people(people_json)