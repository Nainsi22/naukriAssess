import os


def parse_log(file_path):
    """
    Parse the log file and return a dictionary mapping customer IDs to sets of page IDs they visited.

    :param file_path: Path to the log file.
    :return: Dictionary with customer IDs as keys and sets of page IDs as values.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file {file_path} not found.")

    customer_pages = {}
    with open(file_path, 'r') as file:
        for line in file:
            try:
                timestamp, page_id, customer_id = line.strip().split(',')
                if customer_id not in customer_pages:
                    customer_pages[customer_id] = set()
                customer_pages[customer_id].add(page_id)
            except ValueError:
                print(f"Skipping malformed line: {line.strip()}")
    return customer_pages


def find_loyal_customers(day1_log, day2_log):
    """
    Find customers who visited the website on both days and visited at least two unique pages on each day.

    :param day1_log: Path to the log file for day 1.
    :param day2_log: Path to the log file for day 2.
    :return: List of customer IDs who are considered loyal.
    """
    try:
        # Parse both log files
        day1_customers = parse_log(day1_log)
        day2_customers = parse_log(day2_log)
    except FileNotFoundError as e:
        print(e)
        return []

    loyal_customers = []

    # Check for loyal customers
    for customer_id, pages_day1 in day1_customers.items():
        if customer_id in day2_customers:
            pages_day2 = day2_customers[customer_id]
            if len(pages_day1) >= 2 and len(pages_day2) >= 2:
                loyal_customers.append(customer_id)

    return loyal_customers


# Example usage
day1_log_file = 'day1_log.txt'  # Replace with the actual path to the Day 1 log file
day2_log_file = 'day2_log.txt'  # Replace with the actual path to the Day 2 log file

loyal_customers = find_loyal_customers(day1_log_file, day2_log_file)
print('Loyal Customers:', loyal_customers)

