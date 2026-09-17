# Testing Fundamentals
# Definition: Testing is the process of evaluating a system or its components to 
# verify that it meets specified requirements and works as expected.

# Types of Testing
# 1. Unit Testing: Testing individual components ⭐
# 2. Integration Testing: Testing how components work together ⭐
# 3. Functional Testing: Testing the application's functionality
# 4. End-to-End Testing: Testing the complete flow
# 5. Performance Testing: Testing speed and scalability

# ⭐Unit Testing with pytest
# What is pytest?
# pytest is a powerful testing framework for Python that makes it easy to write simple 
# and scalable test cases.
# 
# pip install pytest pytest-cov pytest-xdist ⭐

import pytest
# ===== Simple Functions to Test =====
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# ===== Basic Tests =====
def test_add():
    """Test the add function."""
    assert add(2, 3) == 5 # test script
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# ===== Running Tests =====
# python -m pytest P2.py -v