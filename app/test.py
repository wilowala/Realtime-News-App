from models import Source, News
import unittest

class SourceTest(unittest.TestCase):
    '''Testace to test the Source Class'''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("name","description","url" )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

class NewsTest(unittest.TestCase):
    '''Testace to test the Source Class'''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News("","","","","","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, News))


if __name__ == '__main__':
    unittest.main()