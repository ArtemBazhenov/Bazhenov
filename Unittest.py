from class_DB import DB
import unittest

class TestTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = DB()
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.dbClose()
    
    def setUp(self):
        self.db.newCursor()
    
    def tearDown(self):
        self.db.closeCursor()
    
    def test_get1(self):
        res = [(1, 'towel-pants', 3), (2, 'towel-pants', 3), (3, 'surprisebox', 1), (3, 'towel-pants', 1)]
        self.assertEqual(self.db.get1(), res)
    
    def test_get2(self):
        res = [('Oleg', '+'), ('Alina', '+'), ('Artem', '+')]
        self.assertEqual(self.db.get2(), res)
        
    def test_get3(self):
        res = [('surprisebox', 'mystic'), ('towel-pants', 'clother')]
        self.assertEqual(self.db.get3(), res)
    
if __name__ == '__main__':
    unittest.main(failfast = False)