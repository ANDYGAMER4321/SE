from hypothesis import given, strategies as st
from highway_toll import parse_plate, trip_cost, axle_class


@given(st.text() | st.none())
def test_parse_plate_no_crash(s):
    try:
        parse_plate(s)
    except Exception as e:
        assert False, f"parse_plate crashed with: {e}"


@given(st.text() | st.none())
def test_trip_cost_no_crash(s):
    try:
        trip_cost(s)
    except Exception as e:
        assert False, f"trip_cost crashed with: {e}"


@given(st.text() | st.none())
def test_axle_class_no_crash(s):
    try:
        axle_class(s)
    except Exception as e:
        assert False, f"axle_class crashed with: {e}"


@given(st.integers(max_value=1))
def test_axle_class_invalid_counts(n):
    assert axle_class(str(n)) is None


@given(
    st.integers(max_value=-1),
    st.integers(min_value=0, max_value=10000),
)
def test_trip_cost_rejects_negative(count, rate):
    assert trip_cost(f"{count}x{rate}") is None


@given(
    st.integers(min_value=0, max_value=10000),
    st.integers(min_value=0, max_value=10000),
)
def test_trip_cost_valid_calculation(count, rate):
    assert trip_cost(f"{count}x{rate}") == count * rate
