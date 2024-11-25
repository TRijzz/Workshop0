
# Task 1. Classify Temperatures:

#-->
temperatures = [
    8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
 # 16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 13.4, 8.1,
 # 17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 7.8, 17.5, 13.6, 8.7,
 # 17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 16.4, 12.7, 8.9, 18.2, 13.1, 7.8,
 # 16.6, 12.5
    ]

#empty lists
cold =[] #temperature belpw 10 C
mild = [] #temperature below 10 C and 15 C
comfortable = [] #temperature between 15 C and 20 C

#Iteration:

for temp in temperatures:
  if temp > 10:
    cold.append(temp)
  elif 10 <= temp < 15:
    mild.append(temp)
  elif 15 <= temp < 20:
    comfortable.append(temp)
print("Cold: ", cold)
print("Mild: ", mild)
print("Comfortable: ", comfortable)


#Task 2. Based on Data - Answer all the Questions:
# Q1: How many times was it mild?
mild = len(mild)
print(f"It was mild",mild,"times.")

# Q2: How many times was it comfortable?
comfortable = len(comfortable)
print(f"It was comfortable",comfortable,"times.")

# Q3: How many times was it cold?
cold = len(cold)
print(f"It was cold",cold,"times.")


# Task 3. Convert Temperatures from Celsius to Fahrenheit
# Formula: Fahrenheit = (Celsius ×9/5)+ 32

temperatures = [
    8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5, 16.5,
    12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 13.4, 8.1,
    17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 7.8, 17.5, 13.6,
    8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 16.4, 12.7, 8.9, 18.2,
    13.1, 7.8, 16.6, 12.5
]

temperatures_fahrenheit = []

for temp in temperatures:
  fahrenheit = (temp * 9 / 5 ) + 32
  temperatures_fahrenheit.append(fahrenheit)
print("Temperatures in Fahrenheit: ", temperatures_fahrenheit)


# Task 4. Analyze Temperature Patterns by Time of Day:
import matplotlib.pyplot as plt
temperatures = [
    8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5, 16.5,
    12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 13.4, 8.1,
    17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 7.8, 17.5, 13.6,
    8.7, 17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 16.4, 12.7, 8.9, 18.2,
    13.1, 7.8, 16.6, 12.5
]

night_temps = []
evening_temps = []
day_temps = []
i= 0  #manually tracking the index)
for temp in temperatures:
    if i % 24 < 8:
        night_temps.append(temp)
    elif i % 24 < 16:
        evening_temps.append(temp)
    else:
        day_temps.append(temp)
    i += 1

if len(day_temps) > 0:
    average_day_temp = sum(day_temps) / len(day_temps)
else:
    average_day_temp = 0

print("Night temperatures:", night_temps)
print("Evening temperatures:", evening_temps)
print("Day temperatures:", day_temps)
print("Average daytime temperature:", average_day_temp)


plt.figure(figsize=(10, 6))
plt.plot(range(len(day_temps)), day_temps, label="Daytime Temperatures", color="orange", marker="o")
plt.xlabel("Time (Day Intervals)")
plt.ylabel("Temperature (°C)")
plt.title("Daytime Temperatures")


# 8.1.1 Exercise - Recursion:

# Task 1 - Sum of Nested Lists:
def sum_nested_list(nested_list):
    total = 0
    stack = [nested_list]

    while stack:
        current = stack.pop()
        for element in current:
            if isinstance(element, list):
                 stack.append(element)
            else:
                total += element
    return total

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print("Total sum of nested list:", result)

# Task 2 - Generate All Permutations of a String:
def generate_permutations(s):
    result = []


    if len(s) == 1:
        return [s]

    for i in range(len(s)):

        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            result.append(s[i] + perm)

    return result

print(generate_permutations("abc"))
print(generate_permutations("aab"))

# # Task 3 - Directory Size Calculation:
#Task 1:
def calculate_directory_size(directory):
    total_size = 0

    #iterate in dictionary through each key-value
    for key, value in directory.items():
        if isinstance(value, dict):
            total_size += calculate_directory_size(value)
        else:  #
            total_size += value

    return total_size

directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        }
    }
}


total_size = calculate_directory_size(directory_structure)
print(f"Total size of the directory: {total_size} KB")


# # # 8.2 Dynamic Programming:
def min_coins(coins, amount):
     coins.sort(reverse=True)  #Sorting coins in descending order
    coin_count = 0

    for coin in coins:
        if amount == 0:
            break


        count = amount // coin
        coin_count += count
        amount -= count * coin

    #if the amount is not zero, it's not possible to form it
    return coin_count if amount == 0 else -1
coins = [1, 2, 5]
amount = 11
result = min_coins(coins, amount)
print(f"The minimum number of coins to make {amount} is: {result}")
