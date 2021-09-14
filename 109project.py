import pandas as pd
import csv
import statistics

df = pd.read_csv("109projectdata.csv")
data = df["mathscore"].tolist()
mean = statistics.mean(data)
print("mean is:-",mean)
stdev = statistics.stdev(data)
print("standard deviation is:-",stdev)
mode = statistics.mode(data)
print("mode is:-",mode)
median = statistics.median(data)
print("median is:-",median)

first_standard_deviation_start,first_standard_deviation_end = mean-stdev,mean+stdev
second_standard_deviation_start,second_standard_deviation_end = mean-(2*stdev),mean+(2*stdev)
third_standard_deviation_start,third_standard_deviation_end = mean-(3*stdev),mean+(3*stdev)

list_of_data_first_standard_deviation = [result for result in data if result>first_standard_deviation_start and result<first_standard_deviation_end]
list_of_data_second_standard_deviation = [result for result in data if result>second_standard_deviation_start and result<second_standard_deviation_end]
list_of_data_third_standard_deviation = [result for result in data if result>third_standard_deviation_start and result<third_standard_deviation_end]
print("mean is {}".format(mean))
print("mode is {}".format(mode))
print("median is {}".format(median))
print("stdev is {}".format(stdev))

print("{}% of data lies within 2 standard deviation".format(len(list_of_data_second_standard_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_third_standard_deviation)*100.0/len(data)))

