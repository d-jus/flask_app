import unittest
from neural_network import compute


class SSNTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.table = [1,2,3,4,5,6,0,0]
    def test_ssn_compute(self):
        with self.assertRaises(Exception):
            compute.compute(self.table)


if __name__ == "__main__":
    unittest.main()