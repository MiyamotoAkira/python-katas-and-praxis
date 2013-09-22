import unittest


from katabowling import KataBowling

class KataBowlingTests(unittest.TestCase):
    def test_calculateScore_allStrikes(self):
        kata = KataBowling()
        result = kata.getScore('XXXXXXXXXXXX')
        self.assertEqual(result, 300)

    def test_calculateScore_all9AndMiss(self):
        kata = KataBowling()
        result = kata.getScore('9-9-9-9-9-9-9-9-9-9-')
        self.assertEqual(result, 90)

    def test_calculateScore_allFiveAndSoare(self):
        kata = KataBowling()
        result = kata.getScore('5/5/5/5/5/5/5/5/5/5/')
        self.assertEqual(result, 150)

    def test_getFrames_allStrikes(self):
        kata = KataBowling()
        result = kata.getFrames()


def main():
	suite = unittest.TestLoader().loadTestsFromTestCase(KataBowlingTests)
	unittest.TextTestRunner(verbosity=2).run(suite)
