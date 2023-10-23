def calculate_downpayment(hours: int, rate: int, dividers=1) -> int:
    """Calculates the downpayment for a given number of hours and rate divided by dividers."""

    total_downpayment = hours * rate
    per_head = total_downpayment / dividers

    return per_head


def divide_half_calculate_downpayment(hours: int, rate: int) -> int:
    """Calculates the downpayment for a given number of hours and rate divided by 2."""
    return calculate_downpayment(hours=hours, rate=rate, dividers=2)


MARCO_2023_RATE = 600
november_hours = 7


def print_monthly_downpayment_report(
    month: str, year: int, hours: int, rate=MARCO_2023_RATE, group_name="Dgroup Ballers"
):
    """Print monthly downpayment report."""

    month_downpayment = calculate_downpayment(hours=hours, rate=MARCO_2023_RATE)
    divide_by_2_downpayment = divide_half_calculate_downpayment(hours=hours, rate=rate)
    print(f"\n========== {group_name} Downpayment Calculator ==========\n")
    print(f"{month} {year} total hours:", november_hours)
    print("Rate per Hour: Php", rate)
    print(
        f"Total downpayment: {hours}*{rate} => Php ",
        int(month_downpayment),
    )
    print(
        f"Dodot and Fitz Per head: Php{int(month_downpayment)} / 2 => Php",
        int(divide_by_2_downpayment),
    )
    print("\n===========================================================\n")


print_monthly_downpayment_report(month="November", year=2023, hours=november_hours)
