import matplotlib.pyplot as plt
import pandas as pd
from numpy import sqrt

results_file_path = "/home/user/PycharmProjects/SliceAdmissionControl/total1.csv"

legend = {"iteration",
          "duration_upper_bound",
          "unit_value_beta_params",
          "unit_value_scaler",
          "total_samples",
          "number_of_slots",
          "exp_total_acc",
          "lin_total_acc",
          "fcfs_total_acc",
          ## rev_per_all ##
          "avg_exp_rev_per_all", "avg_lin_rev_per_all", "avg_fcfs_rev_per_all",
          "var_exp_rev_per_all", "var_lin_rev_per_all", "var_fcfs_rev_per_all",
          "exp_rev_per_all_gain", "lin_rev_per_all_gain",
          "var_exp_rev_per_all_gain", "var_lin_rev_per_all_gain",
          ## rev_per_acc ##
          "avg_exp_rev_per_acc", "avg_lin_rev_per_acc", "avg_fcfs_rev_per_acc",
          "var_exp_rev_per_acc", "var_lin_rev_per_acc", "var_fcfs_rev_per_acc",
          "exp_rev_per_acc_gain", "lin_rev_per_acc_gain",
          "var_exp_rev_per_acc_gain", "var_lin_rev_per_acc_gain",
          ## acc_per_all ##
          "avg_exp_acc_per_all", "avg_lin_acc_per_all", "avg_fcfs_acc_per_all",
          "var_exp_acc_per_all", "var_lin_acc_per_all", "var_fcfs_acc_per_all",
          "exp_acc_per_all_gain", "lin_acc_per_all_gain",
          "var_exp_acc_per_all_gain", "var_lin_acc_per_all_gain",
          ## util_per_slot ##
          "avg_exp_util_per_slot", "avg_lin_util_per_slot", "avg_fcfs_util_per_slot",
          "var_exp_util_per_slot", "var_lin_util_per_slot", "var_fcfs_util_per_slot",
          "exp_util_per_slot_gain", "lin_util_per_slot_gain",
          "var_exp_util_per_slot_gain", "var_lin_util_per_slot_gain",
          ## util_per_acc ##
          "exp_util_per_acc_gain", "lin_util_per_acc_gain"}

df = pd.read_csv(results_file_path, ";")

#############################
# For the data to be plotted, the general way to prepare them is the following:
#############################
# Entire dataframe
print(df)

# A list showing the boolean condition used. E.g. where the value 9 is found in "unit_value_scaler"
print(df["unit_value_scaler"] == 9)

# The dataframe but reduced according to a boolean condition
df2 = df[df["unit_value_scaler"] == 9]
print(df2)

# The dataframe but reduced again according to a new boolean condition
df3 = df2[df2["duration_upper_bound"] == 29]
print(df3)

#############################

##################
# Plot 1 settings: Revenue Gain (ExpRP)
##################
# show_only_cases_where = ("unit_value_scaler", 1)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "exp_rev_per_all_gain"
# y7_dimension = "avg_fcfs_rev_per_all"
# confidence1 = ("var_exp_rev_per_all_gain", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 2 settings: Acceptance Ratio (ExpRP)
##################
# show_only_cases_where = ("unit_value_scaler", 1)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "exp_acc_per_all_gain"
# y7_dimension = "avg_fcfs_acc_per_all"
# confidence1 = ("var_exp_acc_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 3 settings: Resource Utilization (ExpRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "exp_util_per_slot_gain"
# y7_dimension = "fcfs_mean_slot"
# confidence1 = ("var_exp_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 4 settings: Revenue Gain (LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_rev_per_all_gain"
# confidence1 = ("var_lin_rev_per_all_gain", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 5 settings: Acceptance Ratio (LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_acc_per_all_gain"
# y7_dimension = "avg_fcfs_acc_per_all"
# confidence1 = ("var_rnd_acc_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 6 settings: Resource Utilization (LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_util_per_slot_gain"
# y7_dimension = "fcfs_mean_slot"
# confidence1 = ("var_lin_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'
#############################

##################
# Plot 7 settings: Revenue Gain (Random)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "rnd_rev_per_all_gain"
# confidence1 = ("var_lin_rev_per_all_gain", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 8 settings: Acceptance Ratio (Random)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "rnd_acc_per_all_gain"
# y7_dimension = "avg_fcfs_acc_per_all"
# confidence1 = ("var_rnd_acc_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 9 settings: Resource Utilization (Random)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "rnd_mean_util_slot_g"
# y7_dimension = "fcfs_mean_slot"
# confidence1 = ("var_lin_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'
#############################

##################
# Plot 10 settings: Revenue Gain (Epsilon-Greedy)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "eps_rev_per_all_gain"
# confidence1 = ("var_lin_rev_per_all_gain", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 11 settings: Acceptance Ratio (Epsilon-Greedy)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "eps_acc_per_all_gain"
# y7_dimension = "avg_fcfs_acc_per_all"
# confidence1 = ("var_eps_acc_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 12 settings: Resource Utilization (Epsilon-Greedy)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "eps_mean_util_slot_g"
# y7_dimension = "fcfs_mean_slot"
# confidence1 = ("var_lin_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'
#############################

##################
# Plot 13 settings: Revenue Gain (UCB)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "ucb_rev_per_all_gain"
# confidence1 = ("var_lin_rev_per_all_gain", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 14 settings: Acceptance Ratio (UCB)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "ucb_acc_per_all_gain"
# y7_dimension = "avg_fcfs_acc_per_all"
# confidence1 = ("var_ucb_acc_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 15 settings: Resource Utilization (UCB)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "ucb_mean_util_slot_g"
# y7_dimension = "fcfs_mean_slot"
# confidence1 = ("var_lin_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'
#############################

##################
# Plot 16 settings: Revenue Gain (OCO)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_rev_per_all_gain"
# confidence1 = ("var_lin_rev_per_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 17 settings: Acceptance Ratio (OCO)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_acc_per_all_gain"
# y7_dimension = "avg_fcfs_acc_per_all"
# confidence1 = ("var_oco_acc_all", "totalSamples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 18 settings: Resource Utilization (OCO)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_util_per_slot_gain"
# y7_dimension = "fcfs_mean_slot"
# confidence1 = ("var_oco_util_per_slot", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [10, 29, 99]
# legend_loc = 'lower right'
#############################

##################
# Plot 19 settings: Revenue Percentage Gain (ExpRP + LinRP)
##################
def RevenuePercentageGain(x):
    show_only_cases_where = ("unit_value_scaler", x)
    x_dimension = "unit_value_beta_params"
    y1_dimension = "lin_rev_per_all_gain"
    y2_dimension = "exp_rev_per_all_gain"
    y3_dimension = "rnd_rev_per_all_gain"
    y4_dimension = "eps_rev_per_all_gain"
    y5_dimension = "ucb_rev_per_all_gain"
    # y6_dimension = "eps_rev_per_all_gain"
    y7_dimension = "avg_fcfs_rev_per_all"
    confidence1 = ("var_lin_rev_per_all", "totalSamples")
    confidence2 = ("var_exp_rev_per_all", "totalSamples")
    confidence3 = ("var_rnd_rev_per_all", "totalSamples")
    confidence4 = ("var_eps_rev_per_all", "totalSamples")
    confidence5 = ("var_ucb_rev_per_all", "totalSamples")
    dimension_of_plotted_lines = "duration_upper_bound"
    # cases_for_plotted_lines = [9, 29, 99]
    legend_loc = 'upper right'
    cases_for_plotted_lines = [10, 30, 100]
    y_label = r'$\frac{\mu-\mu_F}{\mu_F}$'

    return show_only_cases_where, x_dimension, y1_dimension, y2_dimension, y3_dimension, y4_dimension, y5_dimension,\
        y7_dimension, confidence1, confidence2, confidence3, confidence4, confidence5, dimension_of_plotted_lines, \
        cases_for_plotted_lines, legend_loc, y_label


###################
# Acceptance Ratio Gain (ExpRP + LinRP + Random)
###################
def AcceptanceRatioGain(x):
    show_only_cases_where = ("unit_value_scaler", x)
    x_dimension = "unit_value_beta_params"
    y1_dimension = "lin_acc_per_all_gain"
    y2_dimension = "exp_acc_per_all_gain"
    y3_dimension = "rnd_acc_per_all_gain"
    y4_dimension = "eps_acc_per_all_gain"
    y5_dimension = "ucb_acc_per_all_gain"
    # y6_dimension = "oco_acc_per_all_gain"
    y7_dimension = "avg_fcfs_acc_per_all"
    confidence1 = ("var_lin_acc_all", "totalSamples")
    confidence2 = ("var_exp_acc_all", "totalSamples")
    confidence3 = ("var_rnd_acc_all", "totalSamples")
    confidence4 = ("var_eps_acc_all", "totalSamples")
    confidence5 = ("var_ucb_acc_all", "totalSamples")
    dimension_of_plotted_lines = "duration_upper_bound"
    # cases_for_plotted_lines = [9, 29, 99]
    cases_for_plotted_lines = [10, 30, 100]
    legend_loc = 'lower right'
    y_label = r'$\frac{\eta-\eta_F}{\eta_F}$'

    return show_only_cases_where, x_dimension, y1_dimension, y2_dimension, y3_dimension, y4_dimension, y5_dimension, \
        y7_dimension, confidence1, confidence2, confidence3, confidence4, confidence5, dimension_of_plotted_lines, \
        cases_for_plotted_lines, legend_loc, y_label


###################
# Resource Utilization Gain (ExpRP + LinRP + Random)
# ###################
def ResourceUtilizationGain(x):
    show_only_cases_where = ("unit_value_scaler", x)
    x_dimension = "unit_value_beta_params"
    y1_dimension = "lin_mean_util_slot_g"
    y2_dimension = "exp_mean_util_slot_g"
    y3_dimension = "rnd_mean_util_slot_g"
    y4_dimension = "eps_mean_util_slot_g"
    y5_dimension = "ucb_mean_util_slot_g"
    # y6_dimension = "oco_mean_util_slot_g"
    y7_dimension = "fcfs_mean_slot"
    confidence1 = ("var_lin_util_per_slot", "totalSamples")
    confidence2 = ("var_exp_util_per_slot", "totalSamples")
    confidence3 = ("var_rnd_util_per_slot", "totalSamples")
    confidence4 = ("var_eps_util_per_slot", "totalSamples")
    confidence5 = ("var_ucb_util_per_slot", "totalSamples")
    # confidence6 = ("var_oco_util_per_slot", "totalSamples")
    dimension_of_plotted_lines = "duration_upper_bound"
    cases_for_plotted_lines = [10, 30, 100]
    legend_loc = 'lower right' #15
    y_label = r'$\frac{\rho-\rho_F}{\rho_F}$'

    return show_only_cases_where, x_dimension, y1_dimension, y2_dimension, y3_dimension, y4_dimension, y5_dimension, \
        y7_dimension, confidence1, confidence2, confidence3, confidence4, confidence5, dimension_of_plotted_lines, \
        cases_for_plotted_lines, legend_loc, y_label


first = RevenuePercentageGain(1)
second = AcceptanceRatioGain(1)
third = ResourceUtilizationGain(1)
plots = [first, second, third]

# for i in enumerate(plots):
#     print(i[1][0][0])
#     print(i[1][0][1])

for i in enumerate(plots):
    df2 = df[df[i[1][0][0]] == i[1][0][1]]
    fig = plt.figure(figsize=[8.0, 7.0])
    # fig = plt.figure(figsize=[5.0, 3.5])


    for case in i[1][14]:
        df3 = df2[df2[str(i[1][13])] == case]
        updated_y_dimension1 = df3[i[1][2]].div(df3[i[1][7]], axis=0)
        updated_y_dimension2 = df3[i[1][3]].div(df3[i[1][7]], axis=0)
        updated_y_dimension3 = df3[i[1][4]].div(df3[i[1][7]], axis=0)
        updated_y_dimension4 = df3[i[1][5]].div(df3[i[1][7]], axis=0)
        updated_y_dimension5 = df3[i[1][6]].div(df3[i[1][7]], axis=0)
        if case == 10:
            plt.errorbar(df3[str(i[1][1])], updated_y_dimension1,
                         yerr=(3.291 * sqrt(df3[i[1][8][0]] / df3[i[1][8][1]]) / df3[i[1][7]]),
                         label=r'$\zeta$: ' + str(case) + ' (LinRP)',
                         linestyle='-.',
                         capsize=3,
                         color='red'
                         )

            plt.errorbar(df3[i[1][1]], updated_y_dimension2,
                         yerr=(3.291 * sqrt(df3[i[1][9][0]] / df3[i[1][9][1]]) / df3[i[1][7]]),
                         label=r'$\zeta$: ' + str(case) + ' (ExpRP)',
                         linestyle='-',
                         capsize=3,
                         color='lightcoral'
                         )

            plt.errorbar(df3[i[1][1]], updated_y_dimension3,
                         yerr=(3.291 * sqrt(df3[i[1][10][0]] / df3[i[1][10][1]]) / df3[i[1][7]]),
                         label=r'$\zeta$: ' + str(case) + ' (Random)',
                         linestyle='-',
                         capsize=3,
                         color='blue'
                         )

            plt.errorbar(df3[i[1][1]], updated_y_dimension4,
                         yerr=(3.291 * sqrt(df3[i[1][11][0]] / df3[i[1][11][1]]) / df3[i[1][7]]),
                         label=r'$\zeta$: ' + str(case) + ' (Epsilon-Greedy)',
                         linestyle='-',
                         capsize=3,
                         color='green'
                         )

            plt.errorbar(df3[i[1][1]], updated_y_dimension5,
                         yerr=(3.291 * sqrt(df3[i[1][12][0]] / df3[i[1][12][1]]) / df3[i[1][7]]),
                         label=r'$\zeta$: ' + str(case) + ' (UCB1)',
                         linestyle='-',
                         capsize=3,
                         color='purple'
                         )


    plt.legend(loc=str(i[1][15]), prop={'size': 10})
    plt.rcParams.update({'font.size': 10}) # 20
    plt.xlabel(r'$\omega$', fontsize=14)
    plt.ylabel((str(i[1][16])), fontsize=14)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("res_util_all_.pdf", format="pdf", bbox_inches="tight")
    plt.show()
