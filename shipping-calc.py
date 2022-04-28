from cs50 import get_string

total = 0
shipping_cost = 0
international = ""

# Only accepts yes or no answer, single letter or full word
# Will ask again if invalid response
# Capitalizaton doesn't matter because response will be forced into lowercase not matter what
while (international.lower() not in ["y", "yes", "n", "no"]):
    # Get user input
    international = get_string("Is this being shipped international? ")

# Set international status
if international in ["y", "yes"]:
    international = True
else:
    international = False

# Find shipping cost
if international == True:
    shipping_cost += 15
    print("An international fee has been applied")
    print("--------------------")
if int(total) <= 30:
    shipping_cost += 20
elif int(total) <= 50:
    shipping_cost += 10
else:
    shipping_cost += 0

# Get total from user
total = get_string("what is the total of purchase? ")

# Checking for input errors
# -------------------------
# Not an int?: error
try:
    int(total)
except:
    raise ValueError("Total must be a positive integer.")

# Not a positive int?: error
if int(total) <= 0:
    raise ValueError("Total must be a positive integer.")

# Print calculation
print(f"Total cost: ${total}")
print(f"Shipping cost: ${shipping_cost}")
print("--------------------")
print(f"Grand total: ${int(total)+shipping_cost}")

exit()