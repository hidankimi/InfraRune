# test_infrarune.py
"""
Tests for InfraRune module.
"""

import unittest
from infrarune import InfraRune

class TestInfraRune(unittest.TestCase):
    """Test cases for InfraRune class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraRune()
        self.assertIsInstance(instance, InfraRune)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraRune()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
