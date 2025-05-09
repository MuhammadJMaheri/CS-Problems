'''Gets two of the parameters, A, Pb, C and outputs the other using Erlang B formula.
 It has adjustable max values for A and C)'''
from math import floor, factorial
from decimal import Decimal

def p_b(c_in, a_in):
    '''Uses Erlang B formula to calculate probability of blocking for given C and A'''
    sigma = 0
    for no_channels in range(c_in+1):
        sigma += Decimal(a_in**no_channels)/Decimal(factorial(no_channels))
    return float(Decimal(a_in**c_in)/Decimal(factorial(c_in))/sigma)

print('''Choose one of the parameters below to calculate using Erlang B:\n
    1) Pb(GoS/Blocking probability)
    2) A(Total requested traffic intensity)
    3) C(Number of shared channels)\n''')
choice = input("Enter the number corresponding to your choice: ")

match choice:
    case '1':
        total_traffic_intensity = float(input("Enter A(Total requested traffic intensity): "))
        no_shared_channels = int(input("Enter C(Number of shared channels): "))
        blocking_probability = p_b(no_shared_channels, total_traffic_intensity)
        print("Pb(GoS/Blocking probability) = ", blocking_probability)

    #For A and C trial and error method is used
    case '2':
        no_shared_channels = int(input("Enter C(Number of shared channels): "))
        blocking_probability = float(input("Enter Pb(GoS/Blocking probability): "))
        MIN = 0
        MAX = 10**6 #Limits maximum A(traffic intensity), increase this value for greater A
        TOTAL_TRAFFIC_INTENSITY = (MIN + MAX)/2 #inital value
        while abs(p_b(no_shared_channels,TOTAL_TRAFFIC_INTENSITY) - blocking_probability) >= 10**-6:
            if p_b(no_shared_channels, TOTAL_TRAFFIC_INTENSITY) - blocking_probability > 0:
                MAX = (MIN + MAX)/2
                TOTAL_TRAFFIC_INTENSITY = (MIN + MAX)/2
            else :
                MIN = (MIN + MAX)/2
                TOTAL_TRAFFIC_INTENSITY = (MIN + MAX)/2
        print("A(Total requested traffic intensity) = ", TOTAL_TRAFFIC_INTENSITY)
        input("Press enter to exit...")

    case '3':
        total_traffic_intensity = float(input("Enter A(Total requested traffic intensity): "))
        blocking_probability = float(input("Enter Pb(GoS/Blocking probability): "))
        MIN = 0
        MAX = 10**3 #Limits maximum number of trunked channels, increasing it makes factorials huge!
        NO_SHARED_CHANNELS = floor((MIN + MAX)/2) #inital value
        while abs(p_b(NO_SHARED_CHANNELS,total_traffic_intensity) - blocking_probability) >= 10**-4:
            if p_b(NO_SHARED_CHANNELS, total_traffic_intensity) - blocking_probability > 0:
                MIN = floor((MIN + MAX)/2)
                if NO_SHARED_CHANNELS == floor((MIN + MAX)/2):
                    break
                NO_SHARED_CHANNELS = floor((MIN + MAX)/2)
            else :
                MAX = floor((MIN + MAX)/2)
                if NO_SHARED_CHANNELS == floor((MIN + MAX)/2):
                    break
                NO_SHARED_CHANNELS = floor((MIN + MAX)/2)
        print("C(Number of shared channels) = ", NO_SHARED_CHANNELS)
        input("Press enter to exit...")

    case _:
        input("Selected parameter doesn't exist, press enter to exit...")
