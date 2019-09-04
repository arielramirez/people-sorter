
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
            names = [person["name"] for person in get_test_people()]
            self.assertEquals(names, sorted(names))

    def test_sort_by_age_in_names(self):
            orig_people = get_test_people()
            last_person = orig_people[0]
            for curr_person in orig_people[1:]:
                if last_person["name"] == curr_person["name"]:
                    self.assertGreaterEqual(last_person.age, curr_person.age)

    def test_sort_order_when_name_and_age_match(self):
        def get_index(lst, key, value):
            # found on https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
            for i, dic in enumerate(lst):
                if dic[key] == value:
                    return i
            return -1

        orig_people = get_test_people()
        sorted_people = sort_people(orig_people)
        last_person = sorted_people[0]
        for curr_person in sorted_people[1:]:
            if last_person.name == curr_person.name & last_person.age == curr_person.age:
                # ensures that the order in the sorted list matches the order in the original list
                self.assertLess(get_index(orig_people, "ssn", last_person.ssn), get_index(orig_people, "ssn", curr_person.ssn))

    def test_data_integrity(self):
        orig_people = get_test_people()
        sorted_people = sort_people(orig_people)
        # ensure all fields remain and are the same
        # for person in orig_people:
            
                    
            
