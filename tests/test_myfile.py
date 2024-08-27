import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from myfile import armstrong_number

def test_armstrong_number_pass():
    assert armstrong_number(153)

