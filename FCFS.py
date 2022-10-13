import logging

from Node import Node

f = open("fcfs_aar.txt", "w")
f_cpu = open("fcfs_cpu.txt", "w")
f_ram = open("fcfs_ram.txt", "w")
f_sto = open("fcfs_storage.txt", "w")
f_as = open("fcfs_active-slices.txt", "w")
f_revenue_time = open("fcfs_revenue-time.txt", "w")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s\t%(message)s')

system_capacity = list()

def FCFS(NSRs, max_slots, sample_pool, total_requests):
    global system_capacity

    S1 = Node(1, 1, 100, 100, 100)

    system_capacity = [S1[2], S1[3], S1[4]]  # Cloud

    overall_system_util = [0, 0, 0]
    total_util = 0
    no_accepted = 0    
    accumulated_value = 0
    accumulated_squares = 0
    slot = 0
    request_accumulator = 0
    accepted_requests = {}
    expired_slices = []

    while slot < max_slots:
        NSRs_in_current_slot = []

        number_of_requests_in_slot = NSRs[slot]

        first_sub_idx = request_accumulator
        last_sub_idx = request_accumulator + number_of_requests_in_slot

        for sub_idx in range(first_sub_idx, last_sub_idx):
            NSRs_in_current_slot.append(sample_pool[sub_idx])

        request_accumulator += number_of_requests_in_slot

        for request in NSRs_in_current_slot:
            request_value = request[4]

            current_available_system_resources = list(map(lambda x, y: x - y, system_capacity, overall_system_util))
            # print("Current Availability before decision: ", list(np.around(np.array(system_current_available_resources), 2)))

            if all(x < y for x, y in zip(request[0:3], current_available_system_resources)):
                # print("Request Accepted")
                no_accepted += 1

                accepted_requests[no_accepted] = [*request, slot]
                accumulated_value += request_value
                accumulated_squares += request_value ** 2                    

                overall_system_util[0] += request[0]
                overall_system_util[1] += request[1]
                overall_system_util[2] += request[2]            

        # Used to track the expired requests
        expired_requests = []
        # Check for expired slices in the requests list
        for old_request in accepted_requests:
            if slot == accepted_requests[old_request][3] + accepted_requests[old_request][5]:  # reqs_[5] + reqs_[6]
                expired_requests.append(old_request)
                overall_system_util[0] -= accepted_requests[old_request][0]
                overall_system_util[1] -= accepted_requests[old_request][1]
                overall_system_util[2] -= accepted_requests[old_request][2]
                
                # active_slices = [s for s in accepted_requests if s not in expired_slices]
                # print("Number of Active Slices: ", len(active_slices))

        # Remove expired slices from the accepted requests dict
        for expired_request_idx in expired_requests:
            del accepted_requests[expired_request_idx]

        slot += 1
        total_util += sum(overall_system_util)

        current_acceptance_ratio = float(no_accepted) / total_requests
    

    return float(accumulated_value), float(no_accepted), float(total_util), float(accumulated_squares)

#############################################################################################################
#############################################################################################################
def main(max_slots, fixed_NSRs, sample_pool, total_requests):

    return FCFS(fixed_NSRs, max_slots, sample_pool, total_requests)


