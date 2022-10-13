import random
import numpy as np
from numpy.random import default_rng
import ExpRP
import FCFS
import LinRP
import time

max_dur_counter = 9

init_random_seed = random.randint(0, max_dur_counter)
# init_random_seed = random.randint(0, 1000)
# print(init_random_seed)

# rng2 = default_rng(init_random_seed)
rng = default_rng(init_random_seed)
np.random.seed(init_random_seed)

performances = []
all_revenues = list()

# assessed_parameters = {"duration_upper_bound": [1, 50],  # e.g. 15
#                        "unit_value_upper_bound": [1, 10],  # e.g. 1000 lower bound must be greater than 0
#                        "cpu_beta_a": [0, 5],  # e.g. 1
#                        "cpu_beta_b": [0, 5],  # e.g. 0.5
#                        "ram_beta_a": [0, 5],  # e.g. 0.5
#                        "ram_beta_b": [0, 5],  # e.g. 1
#                        "sto_beta_a": [0, 5],  # e.g. 0.2
#                        "sto_beta_b": [0, 5]}  # e.g. 0.8

assessed_parameters = {"duration_upper_bound": [5, 50],  # e.g. 15
                       "unit_value_beta_a": [0.1, 0.1],  # e.g. 1000 lower bound must be greater than 0
                       "unit_value_beta_b": [0.1, 0.1],
                       "cpu_beta_a": [1, 1],  # e.g. 1
                       "cpu_beta_b": [1, 1],  # e.g. 0.5
                       "ram_beta_a": [1, 1],  # e.g. 0.5
                       "ram_beta_b": [1, 1],  # e.g. 1
                       "sto_beta_a": [1, 1],  # e.g. 0.2
                       "sto_beta_b": [1, 1]}  # e.g. 0.8

uv_par_counter = 0.05

unit_value_scaler = 9  # 'Kappa'
system_resource_components = int()
number_of_slots = 50000000
duration_upper_bound = int()  # i.e. from (always) 1 up to duration_upper_bound (inclusive) slots
unit_value_beta_params = [float(), float()]  # i.e. from (always) 1 up to max_unit_value (inclusive) slots
cpu_beta_params = [float(), float()]
ram_beta_params = [float(), float()]
storage_beta_params = [float(), float()]
pmin = 1
pmax = float()  # unit_value_upper_bound

# print("Sampling request specs")
# print(get_request_specs_sample(requests_sample_space, rng))

# utilization_cpu = {"FCFS": {}, "LinRP": {}, "ExpRP": {}}
# utilization_ram = {"FCFS": {}, "LinRP": {}, "ExpRP": {}}
# utilization_storage = {"FCFS": {}, "LinRP": {}, "ExpRP": {}}
# acceptance_ratio = {"FCFS": {}, "LinRP": {}, "ExpRP": {}}
# revenue = {"FCFS": {}, "LinRP": {}, "ExpRP": {}}

fixed_NSRs = list()
# print(fixed_NSRs)
total_samples = sum(fixed_NSRs)
# print(required_samples)


def draw_required_samples(samples, random_generator):
    global duration_upper_bound, cpu_beta_params, ram_beta_params, storage_beta_params, all_revenues, max_dur_counter
    temp_common_drawn_samples = []

    all_revenues = []

    cpu = get_resource_sample(cpu_beta_params, samples)*100
    ram = get_resource_sample(ram_beta_params, samples)*100
    stor = get_resource_sample(storage_beta_params, samples)*100
    unit_values = sample_random_unit_value(samples)

    for i in range(samples):
        dur = random_generator.choice(range(1, max_dur_counter+1))
        all_revenues.append(get_revenue_of_current_request(unit_values[i], cpu[i], ram[i], stor[i], dur))
        temp_common_drawn_samples.append((cpu[i], ram[i], stor[i], dur, all_revenues[i]))

    return temp_common_drawn_samples

def get_resource_sample(resource, n):
    return np.random.beta(resource[0], resource[1], size=n)

# def sample_random_unit_value(n, random_generator):
#     global unit_value_upper_bound
#     list_of_unit_values = []
#     for i in range(n):
#         list_of_unit_values.append(random_generator.uniform(0, unit_value_upper_bound))
#     return list_of_unit_values


def sample_random_unit_value(n):
    global unit_value_beta_params, unit_value_scaler
    list_of_unit_values = []
    for i in range(n):
        list_of_unit_values.append(1 + unit_value_scaler * np.random.beta(unit_value_beta_params[0], unit_value_beta_params[1]))

    return list_of_unit_values

# To be moved to the other modules
def get_revenue_of_current_request(unit_value, cpu, ram, storage, duration):
    return unit_value * (cpu + ram + storage) * duration


def get_random_parameter(param):
    global rng
    return rng.uniform(assessed_parameters[param][0], assessed_parameters[param][1])


def set_new_random_parameters():
    global assessed_parameters, number_of_slots, duration_upper_bound, unit_value_beta_params, cpu_beta_params, \
        ram_beta_params, storage_beta_params, pmax, fixed_NSRs, total_samples, max_dur_counter

    duration_upper_bound = max_dur_counter
    unit_value_beta_params[0] = uv_par_counter
    unit_value_beta_params[1] = uv_par_counter
    cpu_beta_params[0] = get_random_parameter("cpu_beta_a")
    cpu_beta_params[1] = get_random_parameter("cpu_beta_b")
    ram_beta_params[0] = get_random_parameter("ram_beta_a")
    ram_beta_params[1] = get_random_parameter("ram_beta_b")
    storage_beta_params[0] = get_random_parameter("sto_beta_a")
    storage_beta_params[1] = get_random_parameter("sto_beta_b")

    pmax = duration_upper_bound * (unit_value_scaler + 1)
    fixed_NSRs = list(rng.poisson(2, number_of_slots))
    # rng2.shuffle(fixed_NSRs)
    # print(fixed_NSRs)
    total_samples = sum(fixed_NSRs)

iteration = 1

print("{0:>9}".format("iteration"),
      "{0:>8}".format("max_dur"),
      "{0:>5}".format("uv_a"),
      "{0:>5}".format("uv_b"),
      "{0:>10}".format("uv_scaler"),
      "{0:>10}".format("total_req"),
      "{0:>12}".format("exp_acc_req"),
      "{0:>12}".format("lin_acc_req"),
      "{0:>13}".format("fcfs_acc_req"),
      "{0:>19}".format("exp_acc_ratio_gain"),
      "{0:>21}".format("exp_rev_per_all_gain"),
      "{0:>20}".format("std_exp_rev_per_all"),
      "{0:>20}".format("std_lin_rev_per_all"),
      "{0:>21}".format("std_fcfs_rev_per_all"),
      "{0:>20}".format("avg_exp_rev_per_all"),
      "{0:>20}".format("avg_lin_rev_per_all"),
      "{0:>21}".format("avg_fcfs_rev_per_all"),
      "{0:>19}".format("std_exp_rev_per_acc"),
      "{0:>19}".format("std_lin_rev_per_acc"),
      "{0:>20}".format("std_fcfs_rev_per_acc"),
      "{0:>19}".format("avg_exp_rev_per_acc"),
      "{0:>19}".format("avg_lin_rev_per_acc"),
      "{0:>20}".format("avg_fcfs_rev_per_acc"),
      "{0:>21}".format("exp_rev_per_acc_gain"),
      "{0:>28}".format("exp_mean_util_per_slot_gain"),
      "{0:>27}".format("exp_mean_util_per_acc_gain"),
      "{0:>19}".format("lin_acc_ratio_gain"),
      "{0:>21}".format("lin_rev_per_all_gain"),
      "{0:>21}".format("lin_rev_per_acc_gain"),
      "{0:>28}".format("lin_mean_util_per_slot_gain"),
      "{0:>27}".format("lin_mean_util_per_acc_gain"),
      "{0:>15}".format("simulation_dur")
      )

with open(str(unit_value_scaler) + ".csv", "w") as stored_file:
    stored_file.write('{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}\n'.format(
        "iteration",
        "duration_upper_bound",
        "unit_value_beta_params",
        "unit_value_scaler",
        "total_samples",
        "exp_accepted_requests",
        "lin_accepted_requests",
        "fcfs_accepted_requests",
        "exp_acc_ratio_gain",
        "exp_rev_per_all_gain",
        "std_exp_rev_per_all",
        "std_lin_rev_per_all",
        "std_fcfs_rev_per_all",
        "avg_exp_rev_per_all",
        "avg_lin_rev_per_all",
        "avg_fcfs_rev_per_all",
        "std_exp_rev_per_acc",
        "std_lin_rev_per_acc",
        "std_fcfs_rev_per_acc",
        "avg_exp_rev_per_acc",
        "avg_lin_rev_per_acc",
        "avg_fcfs_rev_per_acc",
        "exp_rev_per_acc_gain",
        "exp_mean_util_per_slot_gain",
        "exp_mean_util_per_acc_gain",
        "lin_acc_ratio_gain",
        "lin_rev_per_all_gain",
        "lin_rev_per_acc_gain",
        "lin_mean_util_per_slot_gain",
        "lin_mean_util_per_acc_gain",
        "simulation_dur"))

    while True:
        start_time = time.time()
        set_new_random_parameters()

        common_drawn_samples = draw_required_samples(total_samples, rng)
        # print(common_drawn_samples)
        # print("Evaluating Iteration: ", iteration)

        # print("ExpRP")
        exprp_scores = ExpRP.main(number_of_slots, fixed_NSRs, common_drawn_samples, total_samples, pmin, pmax)

        fcfs_scores = FCFS.main(number_of_slots, fixed_NSRs, common_drawn_samples, total_samples)

        linrp_scores = LinRP.main(number_of_slots, fixed_NSRs, common_drawn_samples, total_samples, pmin, pmax)

        simulation_dur = round(time.time(), 1) - round(start_time, 1)

        # accumulated_value = exprp_scores[0]
        # accumulated_utilization = exprp_scores[2]
        # accumulated_squares = exprp_scores[3]

        exp_accepted_requests = exprp_scores[1]
        fcfs_accepted_requests = fcfs_scores[1]
        lin_accepted_requests = linrp_scores[1]

        avg_exp_rev_per_all = exprp_scores[0] / total_samples
        avg_fcfs_rev_per_all = fcfs_scores[0] / total_samples
        avg_lin_rev_per_all = linrp_scores[0] / total_samples

        avg_exp_rev_per_acc = exprp_scores[0] / exp_accepted_requests
        avg_fcfs_rev_per_acc = fcfs_scores[0] / fcfs_accepted_requests
        avg_lin_rev_per_acc = linrp_scores[0] / lin_accepted_requests

        std_exp_rev_per_all = np.sqrt(exprp_scores[3] / total_samples - avg_exp_rev_per_all**2)
        std_fcfs_rev_per_all = np.sqrt(fcfs_scores[3] / total_samples - avg_fcfs_rev_per_all**2)
        std_lin_rev_per_all = np.sqrt(linrp_scores[3] / total_samples - avg_lin_rev_per_all**2)

        std_exp_rev_per_acc = np.sqrt(exprp_scores[3] / exp_accepted_requests - avg_exp_rev_per_acc**2)
        std_fcfs_rev_per_acc = np.sqrt(fcfs_scores[3] / fcfs_accepted_requests - avg_fcfs_rev_per_acc**2)
        std_lin_rev_per_acc = np.sqrt(linrp_scores[3] / lin_accepted_requests - avg_lin_rev_per_acc**2)

        exprp_acc_ratio = exp_accepted_requests / total_samples
        exprp_rev_per_acc = exprp_scores[0] / exp_accepted_requests
        exprp_mean_util_per_slot = exprp_scores[2] / number_of_slots
        exprp_mean_util_per_acc = exprp_scores[2] / exp_accepted_requests

        fcfs_acc_ratio = fcfs_accepted_requests / total_samples
        fcfs_rev_per_acc = fcfs_scores[0] / fcfs_accepted_requests
        fcfs_mean_util_per_slot = fcfs_scores[2] / number_of_slots
        fcfs_mean_util_per_acc = fcfs_scores[2] / fcfs_accepted_requests

        linrp_acc_ratio = lin_accepted_requests / total_samples
        linrp_rev_per_acc = linrp_scores[0] / lin_accepted_requests
        linrp_mean_util_per_slot = linrp_scores[2] / number_of_slots
        linrp_mean_util_per_acc = linrp_scores[2] / lin_accepted_requests

        exp_acc_ratio_gain = exprp_acc_ratio - fcfs_acc_ratio
        exp_rev_per_all_gain = avg_exp_rev_per_all - avg_fcfs_rev_per_all
        exp_rev_per_acc_gain = exprp_rev_per_acc - fcfs_rev_per_acc
        exp_mean_util_per_slot_gain = exprp_mean_util_per_slot - fcfs_mean_util_per_slot
        exp_mean_util_per_acc_gain = exprp_mean_util_per_acc - fcfs_mean_util_per_acc

        lin_acc_ratio_gain = linrp_acc_ratio - fcfs_acc_ratio
        lin_rev_per_all_gain = avg_lin_rev_per_all - avg_fcfs_rev_per_all
        lin_rev_per_acc_gain = linrp_rev_per_acc - fcfs_rev_per_acc
        lin_mean_util_per_slot_gain = linrp_mean_util_per_slot - fcfs_mean_util_per_slot
        lin_mean_util_per_acc_gain = linrp_mean_util_per_acc - fcfs_mean_util_per_acc

        # print(exprp_scores[1], fcfs_scores[1], linrp_scores[1])

        stored_file.write('{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}\n'.format(
            iteration,
            duration_upper_bound,
            round(unit_value_beta_params[0], 3),
            unit_value_scaler,
            total_samples,
            exp_accepted_requests,
            lin_accepted_requests,
            fcfs_accepted_requests,
            round(exp_acc_ratio_gain, 3),
            round(exp_rev_per_all_gain, 3),
            round(std_exp_rev_per_all, 3),
            round(std_lin_rev_per_all, 3),
            round(std_fcfs_rev_per_all, 3),
            round(avg_exp_rev_per_all, 3),
            round(avg_lin_rev_per_all, 3),
            round(avg_fcfs_rev_per_all, 3),
            round(std_exp_rev_per_acc, 3),
            round(std_lin_rev_per_acc, 3),
            round(std_fcfs_rev_per_acc, 3),
            round(avg_exp_rev_per_acc, 3),
            round(avg_lin_rev_per_acc, 3),
            round(avg_fcfs_rev_per_acc, 3),
            round(exp_rev_per_acc_gain, 3),
            round(exp_mean_util_per_slot_gain, 3),
            round(exp_mean_util_per_acc_gain, 3),
            round(lin_acc_ratio_gain, 3),
            round(lin_rev_per_all_gain, 3),
            round(lin_rev_per_acc_gain, 3),
            round(lin_mean_util_per_slot_gain, 3),
            round(lin_mean_util_per_acc_gain, 3),
            round(simulation_dur, 1)))

        print("{0:>9}".format(iteration),
              "{0:>8}".format(duration_upper_bound),
              "{0:>5}".format(round(unit_value_beta_params[0], 2)),
              "{0:>5}".format(round(unit_value_beta_params[1], 2)),
              "{0:>10}".format(unit_value_scaler),
              "{0:>10}".format(total_samples),
              "{0:>12}".format(exp_accepted_requests),
              "{0:>12}".format(lin_accepted_requests),
              "{0:>13}".format(fcfs_accepted_requests),
              "{0:>19}".format(round(exp_acc_ratio_gain, 2)),
              "{0:>21}".format(round(exp_rev_per_all_gain, 2)),
              "{0:>20}".format(round(std_exp_rev_per_all, 2)),
              "{0:>20}".format(round(std_lin_rev_per_all, 2)),
              "{0:>21}".format(round(std_fcfs_rev_per_all, 2)),
              "{0:>20}".format(round(avg_exp_rev_per_all, 2)),
              "{0:>20}".format(round(avg_lin_rev_per_all, 2)),
              "{0:>21}".format(round(avg_fcfs_rev_per_all, 2)),
              "{0:>19}".format(round(std_exp_rev_per_acc, 2)),
              "{0:>19}".format(round(std_lin_rev_per_acc, 2)),
              "{0:>20}".format(round(std_fcfs_rev_per_acc, 2)),
              "{0:>19}".format(round(avg_exp_rev_per_acc, 2)),
              "{0:>19}".format(round(avg_lin_rev_per_acc, 2)),
              "{0:>20}".format(round(avg_fcfs_rev_per_acc, 2)),
              "{0:>21}".format(round(exp_rev_per_acc_gain, 2)),
              "{0:>28}".format(round(exp_mean_util_per_slot_gain, 2)),
              "{0:>27}".format(round(exp_mean_util_per_acc_gain, 2)),
              "{0:>19}".format(round(lin_acc_ratio_gain, 2)),
              "{0:>21}".format(round(lin_rev_per_all_gain, 2)),
              "{0:>21}".format(round(lin_rev_per_acc_gain, 2)),
              "{0:>28}".format(round(lin_mean_util_per_slot_gain, 2)),
              "{0:>27}".format(round(lin_mean_util_per_acc_gain, 2)),
              "{0:>15}".format(simulation_dur)
              )

        iteration += 1

        uv_par_counter += 0.05
        if round(uv_par_counter, 2) >= 1.05:
            uv_par_counter = 0.05
            max_dur_counter += 2

        # break



