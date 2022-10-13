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
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y_dimension = "exp_rev_per_all_gain"
# confidence = ("var_exp_rev_per_all_gain", "total_samples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 2 settings: Acceptance Ratio (ExpRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y_dimension = "exp_acc_per_all_gain"
# confidence = ("var_exp_acc_per_all_gain", "total_samples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 3 settings: Resource Utilization (ExpRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y_dimension = "exp_util_per_slot_gain"
# confidence = ("var_exp_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 4 settings: Revenue Gain (LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y_dimension = "lin_rev_per_all_gain"
# confidence = ("var_lin_rev_per_all_gain", "total_samples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'upper right'

##################
# Plot 5 settings: Acceptance Ratio (LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y_dimension = "lin_acc_per_all_gain"
# confidence = ("var_lin_acc_per_all_gain", "total_samples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'lower right'

##################
# Plot 6 settings: Resource Utilization (LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y_dimension = "lin_util_per_slot_gain"
# confidence = ("var_lin_util_per_slot_gain", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'lower right'
#############################

##################
# Plot 7 settings: Percentage Gain (ExpRP + LinRP)
##################
# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_rev_per_all_gain"
# y2_dimension = "avg_fcfs_rev_per_all"
# y3_dimension = "exp_rev_per_all_gain"
# confidence = ("var_lin_rev_per_all", "total_samples")
# confidence1 = ("var_exp_rev_per_all", "total_samples")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'upper right'

show_only_cases_where = ("unit_value_scaler", 9)
x_dimension = "unit_value_beta_params"
y1_dimension = "lin_acc_per_all_gain"
y2_dimension = "avg_fcfs_acc_per_all"
y3_dimension = "exp_acc_per_all_gain"
confidence = ("var_lin_acc_per_all", "total_samples")
confidence1 = ("var_exp_acc_per_all", "total_samples")
dimension_of_plotted_lines = "duration_upper_bound"
cases_for_plotted_lines = [9, 29, 99]
legend_loc = 'lower right'

# show_only_cases_where = ("unit_value_scaler", 9)
# x_dimension = "unit_value_beta_params"
# y1_dimension = "lin_util_per_slot_gain"
# y2_dimension = "avg_fcfs_util_per_slot"
# y3_dimension = "exp_util_per_slot_gain"
# confidence = ("var_lin_util_per_slot", "number_of_slots")
# confidence1 = ("var_exp_util_per_slot", "number_of_slots")
# dimension_of_plotted_lines = "duration_upper_bound"
# cases_for_plotted_lines = [9, 29, 99]
# legend_loc = 'lower right'


df2 = df[df[show_only_cases_where[0]] == show_only_cases_where[1]]
# fig = plt.figure(figsize=[5.0, 3.5])
fig = plt.figure(figsize=[6.0, 5.0])

for case in cases_for_plotted_lines:
    df3 = df2[df2[dimension_of_plotted_lines] == case]
    updated_y_dimension = df3[y1_dimension].div(df3[y2_dimension], axis=0)
    updated_y_dimension1 = df3[y3_dimension].div(df3[y2_dimension], axis=0)
    if case == 9:
        plt.errorbar(df3[x_dimension], updated_y_dimension,
                     yerr=(3.291 * sqrt(df3[confidence[0]] / df3[confidence[1]]) / df3[y2_dimension]),
                     label=r'$\zeta$: ' + str(case + 1) + ' (LinRP)',
                     linestyle='-.',
                     capsize=3,
                     color='red'
                     )

        plt.errorbar(df3[x_dimension], updated_y_dimension1,
                     yerr=(3.291 * sqrt(df3[confidence1[0]] / df3[confidence1[1]]) / df3[y2_dimension]),
                     label=r'$\zeta$: ' + str(case + 1) + ' (ExpRP)',
                     linestyle='-',
                     capsize=3,
                     color='lightcoral'
                     )

    if case == 29:
        plt.errorbar(df3[x_dimension], updated_y_dimension,
                     yerr=(3.291 * sqrt(df3[confidence[0]] / df3[confidence[1]]) / df3[y2_dimension]),
                     label=r'$\zeta$: ' + str(case + 1) + ' (LinRP)',
                     linestyle='-.',
                     capsize=3,
                     color='blue'
                     )

        plt.errorbar(df3[x_dimension], updated_y_dimension1,
                     yerr=(3.291 * sqrt(df3[confidence1[0]] / df3[confidence1[1]]) / df3[y2_dimension]),
                     label=r'$\zeta$: ' + str(case + 1) + ' (ExpRP)',
                     linestyle='-',
                     capsize=3,
                     color='lightblue'
                     )

    if case == 99:
        plt.errorbar(df3[x_dimension], updated_y_dimension,
                     yerr=(3.291 * sqrt(df3[confidence[0]] / df3[confidence[1]]) / df3[y2_dimension]),
                     label=r'$\zeta$: ' + str(case + 1) + ' (LinRP)',
                     linestyle='-.',
                     capsize=3,
                     color='green'
                     )

        plt.errorbar(df3[x_dimension], updated_y_dimension1,
                     yerr=(3.291 * sqrt(df3[confidence1[0]] / df3[confidence1[1]]) / df3[y2_dimension]),
                     label=r'$\zeta$: ' + str(case + 1) + ' (ExpRP)',
                     linestyle='-',
                     capsize=3,
                     color='lightgreen'
                     )


# plt.legend(loc=legend_loc)
plt.legend(loc=legend_loc, prop={'size': 10})
plt.rcParams.update({'font.size': 20})
# plt.title(y_dimension + " per " + x_dimension + ". (Group: " + show_only_cases_where[0] + "=" + str(
#     show_only_cases_where[1]) + ")", fontsize=10)
# plt.xlabel(r'$\omega$')
plt.xlabel(r'$\omega$', fontsize=14)
# plt.ylabel(r'$\frac{\mu-\mu_F}{\mu_F}$', fontsize=14)
# plt.ylabel(r'$\frac{\eta-\eta_F}{\eta_F}$', fontsize=14)
plt.ylabel(r'$\frac{\rho-\rho_F}{\rho_F}$', fontsize=14)
# plt.ylabel(r'$\mu_E-\mu_F$')
# plt.ylabel(r'$\mu_L-\mu_F$')
# plt.ylabel(r'$\eta_E-\eta_F$')
# plt.ylabel(r'$\eta_L-\eta_F$')
# plt.ylabel(r'$\rho_E-\rho_F$')
# plt.ylabel(r'$\rho_L-\rho_F$')
plt.tight_layout()
plt.grid(True)
plt.savefig("res_util_all_.pdf", format="pdf", bbox_inches="tight")
plt.show()
