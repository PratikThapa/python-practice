# Data Definition
Tempratures = [20, 19, 23, 24, 25, 21, 18, 
                19, 22, 20, 21, 23, 17, 16,
                18, 19, 21, 24, 26, 25, 
                22, 21, 20, 19, 18, 17, 15, 14, 13,
                45, 32, 33, 34, 31, 39
            ]

# Function to calculate the average temprature

def Average_temprature(temprature):
    if not temprature:
        return "Error!! The temprature cannot be empty."
    return sum(temprature) / len(temprature)


#Function to find the maximum temprature

def Max_temprature(temparture): 
    if not temparture:
        return "Error!! The temprature cannot be empty."
    return max(temparture)

#Function to find the minimum temprature

def Min_temprature(temprature):
    if not temprature:
        return "Error!! The temprature cannot be empty."
    return min(temprature)

#Funtion to count the frequency of temprature

def Frequency_of_Temprature(temprature):
    if not temprature:
        return "Error!! The temprature cannot be empty."
    frequency = {}
    for temp in temprature:
        if not isinstance(temp, (int, float)):
             return "Error!! The temprature list contains invalid data types."
        if temp in frequency:
            frequency[temp] += 1
        else:
            frequency[temp] = 1
        return frequency
    
# Displaying the result of temprature
print("Average temprature: " , Average_temprature(Tempratures))
print("Maximum temprature: " , Max_temprature(Tempratures))
print("Minimum temprature: " , Min_temprature(Tempratures))
print("Frequency of temprature: " , Frequency_of_Temprature(Tempratures))

