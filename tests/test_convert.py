import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from yamlify import convert


class TestYamlify(unittest.TestCase):
    def test_convert_single_file(self):
        # Convert data
        result=convert(
            input_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cars')),
            template_path=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates/template_single.j2')),
            output='output.txt',
            output_filename_template=None
        )
        self.assertIn(result[0]['filename'], 'output.txt')
        self.assertIn(result[0]['content'], 'Toyota Corolla 2020 00001.yaml\nHonda Civic 2019 00002.yaml\nAudi A3 2017 00003.yaml\n')

    def test_convert_multi_files(self):
        # Convert data
        result=convert(
            input_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cars')),
            template_path=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates/template_multi.j2')),
            output=None,
            output_filename_template='{make}.txt'
        )
        print (result)
        self.assertIn(result[0]['filename'], 'Toyota.txt')
        self.assertIn(result[0]['content'], 'Toyota Corolla 2020 00001.yaml')
        self.assertIn(result[1]['filename'], 'Honda.txt')
        self.assertIn(result[1]['content'], 'Honda Civic 2019 00002.yaml')
        self.assertIn(result[2]['filename'], 'Audi.txt')
        self.assertIn(result[2]['content'], 'Audi A3 2017 00003.yaml')

    def test_convert_recursive(self):
        # Convert data
        result=convert(
            input_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')),
            template_path=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates/template_recursive.j2')),
            output='output.txt',
            output_filename_template=None,
            recursive=True
        )
        print (result)
        self.assertIn(result[0]['filename'], 'output.txt')
        self.assertIn(result[0]['content'], 'Corolla\nCivic\nA3\n')


if __name__ == '__main__':
    unittest.main()
