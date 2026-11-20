import pytest
from highway_toll import toll_for, toll_charge, pass_advice


def test_axles_below_minimum():
    with pytest.raises(ValueError):
        toll_for(0, False, False)


def test_two_axles():
    assert toll_for(2, False, False) == 100


def test_three_axles():
    assert toll_for(3, False, False) == 150


def test_four_axles():
    assert toll_for(4, False, False) == 250


def test_other_axles():
    assert toll_for(6, False, False) == 400


def test_peak_true():
    assert toll_for(2, True, False) == 125


def test_peak_false():
    assert toll_for(2, False, False) == 100


def test_fastag_true_two_axles():
    assert toll_for(2, False, True) == 90


def test_fastag_true_other_axles():
    assert toll_for(3, False, True) == 142.5


def test_fastag_false():
    assert toll_for(3, False, False) == 150


def test_exempt_ambulance():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_exempt_fire_engine():
    assert toll_charge("fire_engine", 4, False, False) == 0


def test_non_exempt_vehicle():
    assert toll_charge("car", 2, False, False) == 100


def test_pass_cost_greater():
    assert pass_advice(
        [(False, False), (False, False)], 2, 150
    ) == "buy_pass"


def test_pass_cost_equal():
    assert pass_advice([(False, False)], 2, 100) == "either"


def test_pass_cost_less():
    assert pass_advice([(False, False)], 2, 150) == "pay_per_trip"


def test_no_trips():
    assert pass_advice([], 2, 100) == "pay_per_trip"


def test_multiple_trips():
    trips = [(False, False), (True, False), (False, True)]
    assert pass_advice(trips, 2, 300) == "buy_pass"
