'''A program for estimating pathloss exponent and standard deviation parameters
done by Muhammad Maheri Jolfaei - 402725094'''

import sys
import math
from geopy.distance import geodesic

# Libraries for regression:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def regression(x_arr, y_arr):
    '''Linear regression function using scikit-learn'''

    # Example data
    x = np.array(x_arr)
    y = np.array(y_arr)

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Make predictions
    y_pred = model.predict(x_test)

    # Evaluate the model
    print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
    print("\nEstimated Standard diviation (sigma):", (mean_squared_error(y_test, y_pred))**(0.5))

    # Visualize the results
    output = model.predict(x)
    plt.scatter(x, y, color='blue')
    plt.plot(x, output, color='red')
    plt.xlabel('UE-BS Distance (m)')
    plt.ylabel('Signal power (dBm)')
    plt.title('Linear Regression for signal power')
    print("\nRegression plot is shown, please close the plot for PLE estimation...")
    plt.show()

    # Return
    return output

def distance(lat_bs, lon_bs, lat_ue, lon_ue):
    '''Gives the distance between two coordinates in meters using geopy'''

    coords_bs = (lat_bs, lon_bs)
    coords_ue = (lat_ue, lon_ue)

    return geodesic(coords_bs, coords_ue).m

def ple(d1, p1, d2, p2):
    '''Calculates PLE from two equations'''

    beta = (p1 - p2)/(10 * math.log10(d2 / d1))

    return beta

def main():
    '''Main estimator function'''
    if len(sys.argv) == 1:
        print('''\nFile name is not specified correctly, please specify your file like this example:
            \npython3 estimator.py [FILENAME WITH EXTENSION]\n''')
        return
    file_name = str(sys.argv[1])
    # Or input("Enter filename (with extension):"), can also be given manually

    cell_id = input("Enter cell id: ")
    cell_lat = input("Enter cell latitude: ")
    cell_lon = input("Enter cell longitude: ")

    data = open(file_name)
    data_array = []

    print("\nAll of qualified data for given specs is shown below:\n\nDistance\t RSRP")
    for line in data:

        temp = line.split(",")

        if temp[0] == "sim":
            continue

        if temp[7] == cell_id:
            d = distance(cell_lat, cell_lon, temp[17], temp[18])
            if d >= 300:
                data_array.append(([d], int(temp[16])))
                print("%.2f" % d,"meters\t", temp[16], "dBm")

    print("\nNumber of qualified data:", len(data_array))
    data.close()

    data_array.sort()

    x_array = []
    y_array = []

    for index in data_array:
        x_array.append(index[0])
        y_array.append(index[1])

    power_regression = regression(x_array, y_array)

    max_index = len(x_array) - 1

    print("\nEstimated PLE:", ple(x_array[0][0], power_regression[0],
                                x_array[max_index][0], power_regression[max_index]), "\n")

    return

main()
