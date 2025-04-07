import pytest
from source import shapes

@pytest.fixture

def my_rect():
    return shapes.Rectangle(10,20)

def test_area(my_rect):
    
    assert my_rect.area() == 10*20

def test_perimeter(my_rect):
    
    assert my_rect.perimenter() == (10+20)*2