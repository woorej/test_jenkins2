import pytest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calcul')))
#print(sys.path)
from calculator_server import Calculator

@pytest.fixture
def cal():
    inst = Calculator()
    return inst
    