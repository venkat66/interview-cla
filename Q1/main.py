import re
from datetime import datetime, timedelta

class Customer:
    def __init__(self, enter_time, name, num_tickets):
        self.name = name
        self.enter_time = enter_time
        self.num_tickets = num_tickets
        self.taken_ticket = 0
        self.start_time = None
        self.end_time = None

    def get_customer_time(self):
        return self.end_time - self.start_time

class Counter:
    def __init__(self, capacity, processing_time):
        self.capacity = capacity
        self.processing_time = processing_time
        self.queue = []


def main():
    num_counters = int(input("Number of counters? "))
    queue_capacity = int(input("Queue Capacity? "))
    processing_time = int(input("Processing Time(in seconds)? "))
    
    # customers = [
    #     Customer("2000-01-01 08:00:00", "P1", 1),
    #     Customer("2000-01-01 08:01:00", "P2", 4),
    #     Customer("2000-01-01 08:01:40", "P3", 1),
    #     Customer("2000-01-01 08:03:00", "P4", 1),
    #     Customer("2000-01-01 08:03:00", "P5", 1),
    #     Customer("2000-01-01 08:03:30", "P6", 1)
    # ]
    customers = get_customers()

    counters = calculate_minimum_time(customers, num_counters, queue_capacity, processing_time)

    for customer in customers:
        print(f"Minimum time required for {customer.name} to collect all tickets: {customer.get_customer_time()}")

    open_counters = find_open_counter(counters)
    print("Counter status during operational hours:")
    for counter in open_counters:
        print(counter)


    
def get_customers():
    customers = []
    while True:
       
        print("---------------------------------------------")
        print("Type 'done' to execute the code") 
        queue_data = input("queue data(format:2000-01-01 08:00:00 : P1, 1)? ")

        # Break the loop and return customers when user enters "done"
        if queue_data.lower() == "done":
            return customers
        
        pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) : ([^,:]+), (\d+)"
        match = re.match(pattern, queue_data)
        if match:
            datetime_str = match.group(1)
            name = match.group(2)
            num_tickets = int(match.group(3))
            # adding the initialized customer instance to list
            customers.append(Customer(datetime_str, name, num_tickets))
        else:
            print("Invalid format try again")
     
           

def calculate_minimum_time(customers, num_counters, queue_capacity, processing_time):
    counters = [Counter(queue_capacity, processing_time) for _ in range(num_counters)]
    opening_time = datetime.strptime('2000-01-01 08:00:00', '%Y-%m-%d %H:%M:%S')
    closing_time = datetime.strptime('2000-01-01 08:30:00', '%Y-%m-%d %H:%M:%S')
    total_tickets = 0
    # adding customer to queue where there are less people
    for customer in customers:
        min_counter = min(counters, key=lambda counter: len(counter.queue))
        min_counter.queue.append(customer)
        total_tickets += customer.num_tickets

    queue_number = 1
    last_queue_time = ''
    last_ticket_time = opening_time
    while total_tickets > 0:
        queue_number += 1
        # Breaking loop if we are close to closing time
        if last_ticket_time > closing_time - timedelta(seconds=30):
            break
        # Iterating through counters to issue tickets
        for counter in counters:
            if counter.queue:
                customer = counter.queue[0]
                if customer.start_time is None:
                    customer.start_time = datetime.strptime(customer.enter_time, '%Y-%m-%d %H:%M:%S')
                    last_queue_time = datetime.strptime(customer.enter_time, '%Y-%m-%d %H:%M:%S')
                else:
                    last_queue_time += timedelta(seconds=processing_time)
                if customer.end_time is None:
                    customer.end_time = customer.start_time + timedelta(seconds=processing_time)
                    last_ticket_time = customer.end_time
                else:
                    customer.end_time = last_ticket_time + timedelta(seconds=processing_time)
                    last_ticket_time += timedelta(seconds=processing_time)
                customer.num_tickets -= 1
                customer.taken_ticket +=1

                if customer.num_tickets == 0:
                    counter.queue.pop(0)
                else:
                    counter.queue.append(customer)
                
                print(f"Person in the queue: {customer.name} for ticket {customer.taken_ticket}: Enters in the Queue at {last_queue_time} and gets ticket at {customer.end_time}")
                
                total_tickets -=1

    return counters


def find_open_counter(counters):
    open_counter_times = []
    for i, counter in enumerate(counters, 1):
        if counter.queue:
            open_counter_times.append(f"Counter C{i} is open")
        else:
            open_counter_times.append(f"Counter C{i} is closed")
    return open_counter_times


if __name__ == '__main__':
    main()
