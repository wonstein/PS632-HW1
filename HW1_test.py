import unittest
import HW1

class TestHW1(unittest.TestCase):
	
	def setUp(self):
		return
		
	#Tests
	def test_shout1(self):
		self.assertEqual(HW1.shout("Hey there"), "HEY THERE!")
	
	def test_shout2(self):
		self.assertEqual(HW1.shout("BLAH"), "BLAH!")
		
	def test_shout3(self):
		self.assertEqual(HW1.shout("Blah!"), "BLAH!")
	
	def test_shout4(self):
		self.assertEqual(HW1.shout("Hey. You!"), "HEY! YOU!")
		
	def test_reverse1(self):
		self.assertEqual(HW1.reverse("asdf blah"), "halb fdsa")

	def test_reversewords1(self):
		self.assertEqual(HW1.reversewords("Hi, my name is Blah."), "Blah is name my, Hi.")
	
	def test_reversewordletters1(self):
		self.assertEqual(HW1.reversewordletters("Hi, my name is Blah."), "iH, ym, eman, si, halB")
		
	def test_piglatin1(self):
		self.assertEqual(HW1.piglatin("nix"), "ixnay")

if __name__ == '__main__':
	unittest.main()
		
	