import pytest
from highway_toll import toll_for, toll_charge, pass_advice


def test_two_axle_base():
    assert toll_for(2, False, False) == 100


def test_three_axle_base():
    assert toll_for(3, False, False) == 150


def test_four_axle_base():
    assert toll_for(4, False, False) == 250


def test_other_axle_base():
    assert toll_for(5, False, False) == 400


def test_invalid_axles():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


def test_peak_hour():
    assert toll_for(2, True, False) == 125


def test_fastag_two_axles():
    assert toll_for(2, False, True) == 90


def test_fastag_other_axles():
    assert toll_for(3, False, True) == 142.5


def test_peak_and_fastag():
    assert toll_for(2, True, True) == 112.5


def test_ambulance_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_fire_engine_exempt():
    assert toll_charge("fire_engine", 3, True, True) == 0


def test_regular_vehicle():
    assert toll_charge("car", 2, False, False) == 100


def test_buy_pass():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 150) == "buy_pass"


def test_either_pass():
    trips = [(False, False)]
    assert pass_advice(trips, 2, 100) == "either"


def test_pay_per_trip():
    trips = [(False, False)]
    assert pass_advice(trips, 2, 150) == "pay_per_trip"


def test_empty_trips():
    assert pass_advice([], 2, 100) == "pay_per_trip"
