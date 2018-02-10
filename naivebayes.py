import csv
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

behavior = 'crouches'

file = open(behavior+'.csv', 'r')  # read the dataset
lines = file.readlines()

lines.pop(0)
count = 0
acc_x_list = []
acc_y_list = []
acc_z_list = []
gyro_x_list = []
gyro_y_list = []
gyro_z_list = []
mag_x_list = []
mag_y_list = []
mag_z_list = []

mean_matrix = []
var_matrix = []

window_size = 100
print("# of windows in the data: {}".format(math.ceil(len(lines) / window_size)))

for line in lines:  # read the lines in the file initially
    rawValues = line.split(',')
    acc_x = int(rawValues[1])
    acc_x_list.append(acc_x)
    acc_y = int(rawValues[2])
    acc_y_list.append(acc_y)
    acc_z = int(rawValues[3])
    acc_z_list.append(acc_z)
    gyro_x = int(rawValues[4])
    gyro_x_list.append(gyro_x)
    gyro_y = int(rawValues[5])
    gyro_y_list.append(gyro_y)
    gyro_z = int(rawValues[6])
    gyro_z_list.append(gyro_z)
    mag_x = int(rawValues[7])
    mag_x_list.append(mag_x)
    mag_y = int(rawValues[8])
    mag_y_list.append(mag_y)
    mag_z = int(rawValues[9])
    mag_z_list.append(mag_z)

    if count % window_size == 0:
        mean_row_list = []
        mean_row_list.append(np.mean(acc_x_list))
        mean_row_list.append(np.mean(acc_y_list))
        mean_row_list.append(np.mean(acc_z_list))
        mean_row_list.append(np.mean(gyro_x_list))
        mean_row_list.append(np.mean(gyro_y_list))
        mean_row_list.append(np.mean(gyro_z_list))
        mean_row_list.append(np.mean(mag_x_list))
        mean_row_list.append(np.mean(mag_y_list))
        mean_row_list.append(np.mean(mag_z_list))
        mean_matrix.append(mean_row_list)

        var_row_list = []
        var_row_list.append(np.var(acc_x_list))
        var_row_list.append(np.var(acc_y_list))
        var_row_list.append(np.var(acc_z_list))
        var_row_list.append(np.var(gyro_x_list))
        var_row_list.append(np.var(gyro_y_list))
        var_row_list.append(np.var(gyro_z_list))
        var_row_list.append(np.var(mag_x_list))
        var_row_list.append(np.var(mag_y_list))
        var_row_list.append(np.var(mag_z_list))
        var_matrix.append(var_row_list)

        # avg on each window or the whole?
        acc_x_list = []
        acc_y_list = []
        acc_z_list = []
        gyro_x_list = []
        gyro_y_list = []
        gyro_z_list = []
        mag_x_list = []
        mag_y_list = []
        mag_z_list = []

    count += 1

print("Parsed matrix size: {}".format(np.shape(mean_matrix)))

averaged_mean = np.rint(np.mean(mean_matrix, axis=0))
averaged_var = np.rint(np.mean(var_matrix, axis=0))

variance_mean = np.rint(np.var(mean_matrix, axis=0))
variance_var = np.rint(np.var(var_matrix, axis=0))

print("Mean of Feature mu of "+behavior+" is:")
print(averaged_mean)
print("Mean of Feature var of "+behavior+" is:")
print(averaged_var)

print("Variance of Feature mu of "+behavior+" is:")
print(variance_mean)
print("Variance of Feature var of "+behavior+" is:")
print(variance_var)

outputFileName = "saved_" + behavior + "_params.csv"
with open(outputFileName, 'w', newline='') as outputFile:
    csvWriter = csv.writer(outputFile, delimiter=',')
    csvWriter.writerow(averaged_mean)
    csvWriter.writerow(averaged_var)
    csvWriter.writerow(variance_mean)
    csvWriter.writerow(variance_var)

plt.plot(acc_x_list)
plt.plot(acc_y_list)
plt.plot(acc_z_list)
plt.show()

