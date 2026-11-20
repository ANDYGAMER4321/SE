def parse_plate(plate):
    if not isinstance(plate, str):
        return None

    parts = [p.strip() for p in plate.strip().split('-')]
    if len(parts) != 4:
        return None

    state, district, series, number = parts
    if not (state.isascii() and state.isalpha() and series.isascii() and series.isalpha()):
        return None
    if not (district.isascii() and district.isdigit() and number.isascii() and number.isdigit()):
        return None

    try:
        return state.upper(), int(district), int(number)
    except ValueError:
        return None


def trip_cost(text):
    if not isinstance(text, str):
        return None

    parts = text.strip().lower().split('x')
    if len(parts) != 2:
        return None

    count_str, rate_str = parts[0].strip(), parts[1].strip()
    try:
        count = int(count_str)
        rate = int(rate_str)
    except ValueError:
        return None

    if count < 0 or rate < 0:
        return None

    return count * rate


def axle_class(axles):
    if isinstance(axles, bool) or axles is None:
        return None

    if isinstance(axles, str):
        axles = axles.strip()
    elif not isinstance(axles, int):
        return None

    try:
        n = int(axles)
    except (ValueError, TypeError):
        return None

    if n < 2:
        return None
    if n == 2:
        return 'car'
    if n <= 4:
        return 'truck'
    return 'heavy'


def main():
    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    print("State, District and Number:", result if result is not None else "Invalid plate format")

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    print("Trip Cost:", result if result is not None else "Invalid trip cost format")

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    print("Vehicle Class:", result if result is not None else "Invalid axle count")


if __name__ == "__main__":
    main()
