import unittest
from DictReverser import DictReverser


class TestDictReverser(unittest.TestCase):

    def test_reverse(self):
        input_value = {
            'hired': {
                'be': {
                    'to': {
                        'deserve': 'I'
                    }
                }
            }
        }
        output_value = {
            'I': {
                'deserve': {
                    'to': {
                        'be': 'hired'
                    }
                }
            }
        }

        self.assertEqual(
            DictReverser(input_value).reverse(),
            output_value
        )


if __name__ == '__main__':
    unittest.main()
