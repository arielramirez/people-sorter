import unittest
from sort_people import sort_people
import json

TEST_FILE = 'test_people.json'

def get_test_people():
    with open(TEST_FILE) as json_file:
        orig_people = json.load(json_file)
    return orig_people

class TestPeopleSort(unittest.TestCase):

    def test_sort_by_name(self):
        names = [person["name"] for person in sort_people(get_test_people())]
        self.assertEqual(names, sorted(names))

    def test_sort_by_age_in_names(self):
        sorted_people = sort_people(get_test_people())
        prev_person = sorted_people[0]
        for curr_person in sorted_people[1:]:
            if prev_person["name"] == curr_person["name"]:
                self.assertGreaterEqual(prev_person['age'], curr_person['age'])
            prev_person = curr_person

    def test_sort_order_when_name_and_age_match(self):
        def get_index(lst, key, value):
            # found on https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
            for i, dic in enumerate(lst):
                if dic[key] == value:
                    return i
            return -1

        orig_people = get_test_people()
        sorted_people = sort_people(orig_people)
        prev_person = sorted_people[0]
        for curr_person in sorted_people[1:]:
            if prev_person['name'] == curr_person['name'] and prev_person['age'] == curr_person['age']:
                # ensures that the order in the sorted list matches the order in the original list
                self.assertLess(get_index(orig_people, "ssn", prev_person['ssn']), get_index(orig_people, "ssn", curr_person['ssn']))

    def test_data_integrity(self):
        orig_people = get_test_people()
        sorted_people = sort_people(orig_people)
        for orig_person in orig_people:
            sorted_person_list = [person for person in sorted_people if person['ssn'] == orig_person['ssn'] ]
            self.assertTrue(len(sorted_person_list) == 1)
            sorted_person = sorted_person_list[0]
            for key, value in orig_person.items(): 
                self.assertTrue(sorted_person[key] == value)
            
                    
            
