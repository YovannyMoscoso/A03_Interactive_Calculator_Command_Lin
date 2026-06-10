import sys
from io import StringIO

from app.calculator import Calculator


def run_calculator_with_inputs(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))

    captured_output = StringIO()
    sys.stdout = captured_output

    Calculator.run()

    sys.stdout = sys.__stdout__

    return captured_output.getvalue()


def test_exit_program(monkeypatch):
    output = run_calculator_with_inputs(monkeypatch, ["0"])

    assert "Interactive Calculator" in output
    assert "Exit. Goodbye!" in output


def test_invalid_option(monkeypatch):
    output = run_calculator_with_inputs(monkeypatch, ["9", "0"])

    assert "Invalid option. Please try again." in output
    assert "Exit. Goodbye!" in output


def test_addition(monkeypatch):
    output = run_calculator_with_inputs(monkeypatch, ["1", "10", "5", "0"])

    assert "ADD" in output
    assert "Result: 15.0" in output


def test_invalid_number(monkeypatch):
    output = run_calculator_with_inputs(monkeypatch, ["1", "abc", "0"])

    assert "Invalid number. Please enter numeric values." in output


def test_division_by_zero(monkeypatch):
    output = run_calculator_with_inputs(monkeypatch, ["4", "10", "0", "0"])

    assert "DIVIDE" in output
    assert "Error: Cannot divide by zero." in output