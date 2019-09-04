# Task:
# In the language of your choice, please write a function that takes in a list of unique people and returns a list of the people sorted.
# People have a name, age, and social security number. Their social security number is guaranteed to be unique. 
# The people should be sorted by name (alphabetically) and age (oldest to youngest). 
# When people have the same name and age, they should be sorted in reverse order of how they are in the original list. 

# (When we say “list” you can interpret it as array, list, collection, etc.)
import json
import collections
from classes.quick_sort import QuickSort

#remaining:
# add ability to specify test filename in command line
# add execution instructions to readme
# add more testing data
# clean up code

TEST_FILENAME = 'test_people.json'

# standardizes the data in preparation for sorting
def transform_to_sort_dimensions(raw_people):
	#desired shape of data
	# {name: {
	#	 	age: [ ssn, ssn ],
	#	    age: [ ssn, ssn ]
	#	 }
	# }
	formatted = {}
	for person in raw_people: 
		if person['name'] not in formatted.keys():
			formatted[person['name']] = { person['age']: [person['ssn']] }
		elif person['age'] not in formatted[person['name']].keys():
			formatted[person['name']][person['age']] = [ person['ssn'] ]
		else:
			formatted[person['name']][person['age']].append(person['ssn'])
	return formatted

# this returns the results to the i/o format after sorting
def format_sort_results(sorted_people):
	#input/output format
    # [ 
	#    {
	#	 	"ssn": "123-45-6789"
	#	 	"name": "test",
	#	 	"age": 100,
	#    }
    # ]
	# name dimension
	formatted_people = []
	for name, name_dim in sorted_people.items():
		for age, ssn_arr in name_dim.items():
			for ssn in (ssn_arr if isinstance(ssn_arr, list) else [ssn_arr]):
				formatted_people.append({"ssn": ssn, "name": name, "age": age})
	return formatted_people

# sorting helper function to keep primary script clean
def quickSortList(unsorted_list, sort_function = None):
	sorter = QuickSort()
	if sort_function:
		sorter.sort_function = sort_function
	return sorter.sort(unsorted_list, 0, len(unsorted_list) - 1)

# sorting implementation
def sort_people(raw_people):
	#ensure list is not empty
	if not raw_people:
		return []

	# create list of people indexed by name, then indexed by age (see function for format)
	unsorted_people = transform_to_sort_dimensions(raw_people)

	# sort by name, sorts asc by default
	sorted_names_list = quickSortList(list(set(unsorted_people.keys())))

	# ensure the final sort order is maintained
	sorted_people = collections.OrderedDict()

	for name in sorted_names_list:
	    # get the sorted ages in desc order within a given name
		sorted_ages_list = quickSortList(list(set(unsorted_people[name].keys())), lambda a,b: a > b)
		sorted_people[name] = {}
		for age in sorted_ages_list:
			# storing everything in sorted order by name and age
			sorted_people[name][age] = unsorted_people[name][age]
			# reversing original order of SSNs given
			sorted_people[name][age].reverse()

	# returning the results to their original format (totally optional)
	return format_sort_results(sorted_people)

with open(TEST_FILENAME) as json_file:
	people_json = json.load(json_file)
	sort_people(people_json)
