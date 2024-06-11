import unittest
from model.amenities import Amenities


class TestAmenities(unittest.TestCase):
    def test_create_amenity(self):
        """test creating an amenity"""
        amenity = Amenities(name="Wi-Fi", description="HIgh Speed")
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertEqual(amenity.description, "HIgh Speed")
        self.assertEqual(type(amenity), Amenities)
        
    def test_create_amenity_without_description(self):
        """test create an amenity without description"""
        amenity = Amenities(name="Wi-Fi", description=None)
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertEqual(amenity.description, None)
        self.assertEqual(type(amenity), Amenities)
    
    
    if __name__ == "__main__":
        unittest.main()
