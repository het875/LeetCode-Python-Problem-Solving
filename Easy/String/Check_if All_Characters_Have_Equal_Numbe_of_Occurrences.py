
# 1941. Check if All Characters Have Equal Number of Occurrences

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = {}
        for i in s:
            if i in frequency :
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        print(frequency)
        if max(frequency.values()) == min(frequency.values()):
            print(True)
            return True
        else:
            print(False)
            return False

s = Solution()
s.areOccurrencesEqual("abacbc")
s.areOccurrencesEqual("aaabb")
s.areOccurrencesEqual("aaabbcc")
s.areOccurrencesEqual("aaabbccc")
s.areOccurrencesEqual("aaabbcccc")

# Output:
# {'a': 2, 'b': 2, 'c': 1}
# False
# {'a': 3, 'b': 2}
# False
# {'a': 3, 'b': 2, 'c': 2}
# True
# {'a': 3, 'b': 2, 'c': 3}
# False
# {'a': 3, 'b': 2, 'c': 4}
# False




#Using a simple dictionary to count and compare frequencies
def check_frequency(numbers):
    frequency = {}
    
    # Count the frequency of each number
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Get the frequency values
    freq_values = list(frequency.values())
    
    # Check if all frequencies are equal
    if len(set(freq_values)) == 1:
        print("All numbers have the same frequency.")
    else:
        print("Not all numbers have the same frequency.")

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
check_frequency(numbers)


# Using a dictionary and comparing max and min values
def check_frequency(numbers):
    frequency = {}
    
    # Count the frequency of each number
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Get the frequency values
    freq_values = list(frequency.values())
    
    # Check if the max and min frequency are the same
    if max(freq_values) == min(freq_values):
        print("All numbers have the same frequency.")
    else:
        print("Not all numbers have the same frequency.")

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
check_frequency(numbers)





# Using a dictionary and manually checking all frequencies
def check_frequency(numbers):
    frequency = {}
    
    # Count the frequency of each number
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Get the frequency values
    freq_values = list(frequency.values())
    
    # Check if all frequencies are equal
    for i in range(1, len(freq_values)):
        if freq_values[i] != freq_values[i - 1]:
            print("Not all numbers have the same frequency.")
            return
    
    print("All numbers have the same frequency.")


# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
check_frequency(numbers)




#. Using a dictionary and all() function

def check_frequency(numbers):
    frequency = {}
    
    # Count the frequency of each number
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Get the frequency values
    freq_values = list(frequency.values())
    
    # Check if all frequencies are equal
    if all(value == freq_values[0] for value in freq_values):
        print("All numbers have the same frequency.")
    else:
        print("Not all numbers have the same frequency.")

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
check_frequency(numbers)



#In this method, we check if all the values in the dictionary have the same frequency by comparing th
def check_frequency(numbers):
    frequency = {}
    
    # Count the frequency of each number
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Get the list of frequencies
    freq_values = list(frequency.values())
    
    # Check if all frequencies are the same by comparing every frequency value
    for i in range(1, len(freq_values)):
        if freq_values[i] != freq_values[0]:
            print("Not all numbers have the same frequency.")
            return
    
    print("All numbers have the same frequency.")

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
check_frequency(numbers)

