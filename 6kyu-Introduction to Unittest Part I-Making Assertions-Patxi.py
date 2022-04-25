from unittest import TestCase


class TestPhoneBook(TestCase):

    def setUp(self):
        self.phone_book = PhoneBook()

    def test_create_method(self):
        self.phone_book.create("User", "1234-5678")
        self.assertEqual(self.phone_book["User"], "1234-5678")

    def test_retrieve_method_when_the_name_exists(self):
        self.phone_book.create("Bob", "12345")  # create new name
        self.assertEqual(self.phone_book.retrieve("Bob"), "12345")  # Test retrieve when name exists

    def test_retrieve_method_when_the_name_does_not_exist(self):
        try:
            self.phone_book.retrieve("Random")
        except KeyError as k:
            self.assertEqual(str(k), "'Name not found!'")

    def test_update_method_when_the_name_exists(self):
        self.phone_book.create("Mary", "123456")
        new_number = "1234567"
        self.phone_book.update("Mary", new_number)
        self.assertEqual(self.phone_book["Mary"], new_number)

    def test_delete_method_when_the_name_exists(self):
        self.phone_book.create("Edd", "1")
        self.phone_book.delete("Edd")
        with self.assertRaises(KeyError):
            self.phone_book.retrieve("Edd")
