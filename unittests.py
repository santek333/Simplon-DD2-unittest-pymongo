import unittest
from pymongo import MongoClient

from MongoDB import Film, Actor

class TestFilmMethods(unittest.TestCase):

    def test_get_nb_films(self):
        self.assertEqual(Film.get_nb_films(db), 450)

    def test_get_nb_actors(self):
        self.assertEqual(Actor.get_nb_actors(db), 18023)

    def test_get_actors(self):

        film = Film('tt6674514')
        self.assertEqual(film.get_actors(db), [ " Kangaroo Dundee\n", " Terri Irwin\n", " Phil Wollen\n", " Tim Flannery\n", " Peter Singer\n" ])

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    unittest.main()

    client.close()

