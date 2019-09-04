
# People Sorter

### Goal
Write a function that takes in a list of unique people and returns a list of the people sorted.
People have a name, age, and social security number. Their social security number is guaranteed to be unique. 
The people should be sorted by name (alphabetically) and age (oldest to youngest). 

When people have the same name and age, they should be sorted in reverse order of how they are in the original list. 

### Solution
This solution isolates the name and age and sorts them using a Quick Sort algorithm. It takes these steps:

1. Convert given data into a normalized data format
2. Sort names
3. Sort by age within each name
4. Build sorted dict using sorted lists
5. Reverse order of any duplicate SSNs for a given name and age
6. Reformat sorted data into original data structure (optional) 

The data is then printed to the command line.

The Quick Sort algorithm was adapted from the implementation on this website: [https://www.geeksforgeeks.org/python-program-for-quicksort/](https://www.geeksforgeeks.org/python-program-for-quicksort/)

### Usage
This solution is executed via the command line.

It solution accepts a filename containing a set of JSON data. It outputs the sorted data to the screen in the same format given. 

The test file, `test_people.json` has been inclued for ease of use.

To execute using the testing file:

```
python sort_people.py
```

To execute using another selected file:

```
python sort_people.py --filename 'filename goes here.json'
```

This solution includes some basic unit tests. Use this command to execute the tests:

```
python -m unittest test_sort_people.TestPeopleSort
```

Here is the template of the expected contents for the JSON file:
```
[
	{
		"ssn": "123-45-6789"
		"name": "test",
		"age": 100,
	},
	{
		"ssn": "111-22-333"
		"name": "test",
		"age": 100,
	},
}
```

### Assumptions
- Social security number is unique
- The only pieces of data are SSN, name and age
- Any other person metadata will be lost during the sorting process