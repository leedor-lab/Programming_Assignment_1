"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1
from math import sqrt

class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
       self.assertEqual(hw1.vowel_count("Orange"),3)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""),0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual(hw1.short_lists(([[5], [9, 2], [], [6, 7, 8], [99, 1096]])),[[9,2] , [99,1096]])
        

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [3,2,1], []]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[9,2],[8,3]]), [[2,9], [3,8]])
    
    def test_ascending_pairs_other_lengths_unchanged(self):
         self.assertEqual(hw1.ascending_pairs([[3,1,2],[3],[7,4,6]]), [[3,1,2],[3],[7,4,6]])
    
    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(6,20), data.Price(2,30)),  data.Price(8,50))

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(1,75), data.Price(1,50)),  data.Price(3,25))
   
    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
       self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(1,5), data.Point(3,4))),2 )
    def test_rectangle_area_negative_coordinates(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-6,5), data.Point(3,-2))),63 )
    
    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        self.assertEqual(hw1.books_by_author("William Golding", [data.Book(["William Shakespeare"], "Hamlet"), data.Book(["William Golding"], "Lord of the Flies"), data.Book(["Lois Lowry"], "The Giver")]), [data.Book(["William Golding"], "Lord of the Flies")])

    def test_books_by_author_no_matches(self):
        self.assertEqual(hw1.books_by_author("Leedor Hatzav", [data.Book(["William Shakespeare"],"Hamlet" ),data.Book(["William Golding"],"Lord of the Flies"), data.Book(["Lois Lowry"],"The Giver" )]), [])
        

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(1,5), data.Point(5,1))), data.Circle(data.Point(3,3), sqrt(8)))

    def test_circle_bound_non_square_rectangle(self):
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0,6), data.Point(8,0))), data.Circle(data.Point(4,3), 5))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        self.assertEqual(hw1.below_pay_average([data.Employee("Patrick" , 20),data.Employee("Jeremiah",10), data.Employee("Daniel", 30)]),["Jeremiah"])

    def test_above_pay_average_empty_list(self):
         self.assertEqual(hw1.below_pay_average([]), [])

if __name__ == '__main__':
    unittest.main()
