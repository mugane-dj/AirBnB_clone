#!/usr/bin/python3
"""Defines unittests for Amenity class"""


import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantation(unittest.TestCase):
    """Unittests for Amenity class instances"""

    def test_instance_with_no_args(self):
        cls_type = type(Amenity())
        self.assertEqual(Amenity, cls_type)

    def test_new_instance_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_of_type_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime_obj(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime_obj(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_of_type_str(self):
        self.assertEqual(str, type(Amenity().name))

    def test_new_instance_with_args(self):
        new_obj = Amenity(None, "6")
        self.assertNotIn(None, new_obj.__dict__.values())
        self.assertNotIn("6", new_obj.__dict__.values())

    def test_new_instance_with_kwargs(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = Amenity(id="68976", created_at=dt_iso_format,
                          updated_at=dt_iso_format)
        self.assertEqual(new_obj.id, "68976")
        self.assertEqual(new_obj.created_at, dt)
        self.assertEqual(new_obj.updated_at, dt)

    def test_new_instance_with_args_and_kwargs(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = Amenity(None, id="68976", created_at=dt_iso_format,
                          updated_at=dt_iso_format)
        self.assertNotIn(None, new_obj.__dict__.values())
        self.assertEqual(new_obj.id, "68976")
        self.assertEqual(new_obj.created_at, dt)
        self.assertEqual(new_obj.updated_at, dt)

    def test_str_repr(self):
        new_obj = Amenity()
        new_obj.id = "68976"
        new_obj_str = new_obj.__str__()
        self.assertIn("[Amenity] (68976)", new_obj_str)
        self.assertIn("'id': '68976'", new_obj_str)


class TestAmenity_save(unittest.TestCase):
    """ Unittests for save method in Amenity class"""

    def test_save_with_arg(self):
        new_obj = Amenity()
        with self.assertRaises(TypeError):
            new_obj.save("NaN")

    def test_saves_to_file(self):
        new_obj = Amenity()
        new_obj.save()
        new_obj_id = new_obj.id
        new_obj_created = new_obj.created_at
        with open("file.json", "r") as f:
            json_str = f.read()
            self.assertIn(new_obj_id, json_str)
            self.assertIn(new_obj_created.isoformat(), json_str)


class TestAmenity_to_dict(unittest.TestCase):
    """ Unittests for to_dict method in Amenity class"""
    def test_to_dict_with_arg(self):
        new_obj = Amenity()
        with self.assertRaises(TypeError):
            new_obj.to_dict(None)

    def test_to_dict_contains_kwargs(self):
        new_obj = Amenity()
        new_obj.first_name = "Albert"
        new_obj.last_name = "Einstein"
        self.assertIn("Albert", new_obj.to_dict().values())
        self.assertIn("Einstein", new_obj.to_dict().values())

    def test_to_dict_type_is_dict(self):
        new_obj = Amenity()
        self.assertTrue(dict, type(new_obj.to_dict()))

    def test_to_dict_correct_output(self):
        dt = datetime.now()
        dt_iso_format = dt.isoformat()
        new_obj = Amenity(id="68976", created_at=dt_iso_format,
                          updated_at=dt_iso_format)
        expected = {
            "__class__": "Amenity",
            "id": "68976",
            "created_at": dt_iso_format,
            "updated_at": dt_iso_format
        }
        self.assertEqual(expected, new_obj.to_dict())


if __name__ == "__main__":
    unittest.main()
