import unittest
import kadane


class MyTestCase(unittest.TestCase):
    def test_Prefix(self):
        sequence = [2, 13, 18, -22, -12]
        sums = kadane.prefix(sequence)
        self.assertEqual(sums, [2, 15, 33, 11, -1])

    def test_Max_Sub_Slow(self):
        sequence = [2, 13, 18, -22, 12]
        mss = kadane.maxsubslow(sequence)
        self.assertEqual(mss, (33, 0, 2))

    def test_Max_Sub_Faster(self):
        sequence = [2, 13, 18, -22, 12]
        msfr = kadane.MaxSubFaster(kadane.prefix(sequence))
        self.assertEqual(msfr, (33, 0, 2))

    def test_hocus_pocus(self):
        sequence = [2, 13, 18, -22, 12]
        msfs = kadane.kadane_alg(sequence)
        self.assertEqual(msfs, (33, 0, 2))


if __name__ == "__main__":
    unittest.main()
