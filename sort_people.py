# Task:
#In the language of your choice, please write a function that takes in a list of unique people and returns a list of the people sorted. People have a name, age, and social security number. Their social security number is guaranteed to be unique. The people should be sorted by name (alphabetically) and age (oldest to youngest). When people have the same name and age, they should be sorted in reverse order of how they are in the original list. (When we say “list” you can interpret it as array, list, collection, etc.)
import json
import collections




#input/output format
# [ 
	# {
	# 	"ssn": "123-45-6789"
	# 	"name": "test",
	# 	"age": 100,

	# }
# ]

# sorting format
# {name: [
# 	age: [ ssn, ssn ],
#   age: [ ssn, ssn]
# ]}

# this returns the results to the i/o format after sorting
def format_sort_results(sorted_people):
	# name dimension
	formatted_people = []
	for name, name_dim in sorted_people.items():
		for age, ssn_arr in name_dim.items():
			for ssn in (ssn_arr if isinstance(ssn_arr, list) else [ssn_arr]):
				formatted_people.append({"name": name, "age": age, "ssn": ssn})
	return formatted_people

def sort_people_better(raw_people):
	if not raw_people:
		return []

	# create list of people indexed by name, then indexed by age (see format above)
	unsorted_people = transform_to_sort_dimensions(raw_people)

	# sort by name
	sorted_names = quickSortList(unsorted_people.keys())

	# ensure the order is maintained
	people_sorted_by_name = collections.OrderedDict()

	# for each sorted name
	for name in sorted_names:
	    # get the sorted ages 
		people_sorted_by_name[name] = quickSortList(unsorted_people['name'])

	# returning the results to their original format
	return format_sort_results(people_sorted_by_name)

# stub, uses quick sort to order the list
def quickSortList(unsorted_list):
	return quickSort(unsorted_list)

# incomplete
# based on psuedocode in https://www.geeksforgeeks.org/python-program-for-quicksort/
def quickSort(people, low, high):
	if (low < high):
		partition(people, low, high)
# incomplete


# incomplete
def partition(people, low, high):
	i = low - 1
	pivot = arr[high]
# incomplete

# standardizes the data in preparation for sorting
def transform_to_sort_dimensions(raw_people):
	#desired shape of data
	# {name: [
	#	 	age: [ ssn, ssn ],
	#	    age: [ ssn, ssn ]
	#	 ]
	# }
	formatted = {}
	for person in raw_people: 
		if person['name'] not in formatted.keys():
			formatted[person['name']] = [ person['age']: [person['ssn']] ]
		elif person['age'] not in formatted[person['name']].keys():
			formatted[person['name']][person['age']]  = person['ssn']
		else:
			formatted[person['name']][person['age']].append(person['ssn'])
	return formatted


with open('ep_4_people.json') as json_file:
	people_json = json.load(json_file)
	# sort_people(people_json)
	sort_format = transform_to_sort_dimensions(people_json)
	formatted_sort_results = format_sort_results(sort_format)



## TOO SLOW
# def sort_people_initial(raw_people):

# 	sorted_people = {}
# 	for person in raw_people:
# 		# if the name already exists, insert it into that subset
# 		if person['name'] in sorted_people:
# 			# if the age already exists, append it to the end of the existing list to maintain order
# 			if person['age'] in sorted_people[person['name']]:
# 				# append to the end of the existing list to maintain original order
# 				sorted_people[person['name']][person['age']].append(person['ssn'])
# 			else:
# 				#if the age doesn't exist yet, figure out where to put it
# 				sorted_people['name'] = insertIntoSortedList(sorted_people[person['name']], person)
# 		else:
# 			#if the name doesn't exist yet, figure out where to put it
# 			sorted_people = insertIntoSortedList(sorted_people, person)

# 	# returning the results to their original format
# 	return format_sort_results(sorted_people)

# # https://stackoverflow.com/questions/26135900/inserting-an-element-into-an-array-in-sorted-order
# def insertIntoSortedList(arr, int k, int start, int end) {
#             if (k == 0)
#                 return 0;

#             int mid = (start + end) / 2;

#             if (k > arr[mid] && k < arr[mid + 1])
#                 return mid + 1;

#             if (arr[mid] < k)
#                 return findIndexToBeInserted(arr, k, mid + 1, end);

#             return findIndexToBeInserted(arr, k, start, mid - 1);
#         }
#     }


# with open('ep_4_people.json') as json_file:
# 	people_json = json.load(json_file)
# 	people = sort_people(people_json)
# 		#find out if name exists. 
# 			# If name does not exist, insert it (quick sort?)
# 			# else
# 				# Check if this age exists
# 					#If not, insert it (quick sort?)
# 					#if it does, append it to the end
		
# 	return people
