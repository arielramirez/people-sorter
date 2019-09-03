# Task:
#In the language of your choice, please write a function that takes in a list of unique people and returns a list of the people sorted. People have a name, age, and social security number. Their social security number is guaranteed to be unique. The people should be sorted by name (alphabetically) and age (oldest to youngest). When people have the same name and age, they should be sorted in reverse order of how they are in the original list. (When we say “list” you can interpret it as array, list, collection, etc.)
import json

with open('ep_4_people.json') as json_file:
	people_json = json.load(json_file)
	sort_people(people_json)

#input/output format
# [ 
	# {
	# 	"ssn": "123-45-6789"
	# 	"name": "test",
	# 	"age": 100,

	# }
# ]

# sorting format
# {name: {
# 	age: [ ssn, ssn ],
#   age: [ ssn, ssn]}}

# this returns the results to the i/o format after sorting
def format_sort_results(sorted_people):
	# name dimension
	formatted_people = []
	for name, name_dim in sorted_people:
		for age, ssn_arr in name_dim:
			for ssn in ssn_arr:
				formatted_people.append({"name": name, "age": age, "ssn": ssn})
	return formatted_people

def sort_people(raw_people):

	sorted_people = {}
	for person in raw_people:
		# if the name already exists, insert it into that subset
		if person['name'] in sorted_people:
			# if the age already exists, append it to the end of the existing list to maintain order
			if person['age'] in sorted_people[person['name']]:
				# append to the end of the existing list to maintain original order
				sorted_people[person['name']][person['age']].append(person['ssn'])
			else:
				#if the age doesn't exist yet, figure out where to put it
				sorted_people['name'] = insertIntoSortedList(sorted_people[person['name']], person)
		else:
			#if the name doesn't exist yet, figure out where to put it
			sorted_people = insertIntoSortedList(sorted_people, person)

	# returning the results to their original format
	return format_sort_results(sorted_people)

# https://stackoverflow.com/questions/26135900/inserting-an-element-into-an-array-in-sorted-order
def insertIntoSortedList(arr, int k, int start, int end) {
            if (k == 0)
                return 0;

            int mid = (start + end) / 2;

            if (k > arr[mid] && k < arr[mid + 1])
                return mid + 1;

            if (arr[mid] < k)
                return findIndexToBeInserted(arr, k, mid + 1, end);

            return findIndexToBeInserted(arr, k, start, mid - 1);
        }
    }


with open('ep_4_people.json') as json_file:
	people_json = json.load(json_file)
	people = sort_people(people_json)
		#find out if name exists. 
			# If name does not exist, insert it (quick sort?)
			# else
				# Check if this age exists
					#If not, insert it (quick sort?)
					#if it does, append it to the end
		
	return people
