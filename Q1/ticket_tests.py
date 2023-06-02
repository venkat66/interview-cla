import pytest
from main import Customer, Counter, calculate_minimum_time, find_open_counter

def test_calculate_minimum_time():
    # Test case 1
    customers = [
        Customer("2000-01-01 08:00:00", "P1", 1),
        Customer("2000-01-01 08:01:00", "P2", 4),
        Customer("2000-01-01 08:01:40", "P3", 1),
        Customer("2000-01-01 08:03:00", "P4", 1),
        Customer("2000-01-01 08:03:00", "P5", 1),
        Customer("2000-01-01 08:03:30", "P6", 1)
    ]
    num_counters = 2
    queue_capacity = 4
    processing_time = 30
    counters = calculate_minimum_time(customers, num_counters, queue_capacity, processing_time)
    assert len(counters) == num_counters

    # Test case 2 (additional test)
    customers = [
        Customer("2000-01-01 08:00:00", "P1", 1),
        Customer("2000-01-01 08:01:00", "P2", 1),
        Customer("2000-01-01 08:02:00", "P3", 1)
    ]
    num_counters = 1
    queue_capacity = 2
    processing_time = 30
    counters = calculate_minimum_time(customers, num_counters, queue_capacity, processing_time)
    assert len(counters) == num_counters

def test_find_open_counter():
    # Test case 1
    counters = [
        Counter(4, 30),
        Counter(4, 30),
        Counter(4, 30)
    ]
    open_counters = find_open_counter(counters)
    assert open_counters == ["Counter C1 is closed", "Counter C2 is closed", "Counter C3 is closed"]

    # Test case 2 (additional test)
    counters = [
        Counter(4, 30),
        Counter(4, 30),
        Counter(4, 30)
    ]
    counters[0].queue.append(Customer("2000-01-01 08:00:00", "P1", 1))
    open_counters = find_open_counter(counters)
    assert open_counters == ["Counter C1 is open", "Counter C2 is closed", "Counter C3 is closed"]

if __name__ == "__main__":
    pytest.main()
