from cs50 import get_string
from cs50 import get_int

total = 0
shipping_cost = 0
international = ""

# Only accepts yes or no answer, single letter or full word
# Will ask again if invalid response
# Capitalizaton doesn't matter because response will be forced into lowercase not matter what
while (international.lower() not in ["y", "yes", "n", "no"]):
    # Get user input
    international = get_string("Is this being shipped international? ")

# International fee if applicable
if international in ["y", "yes"]:
    shipping_cost += 15
    print("An international fee has been applied")
    print("--------------------")

# Get total from user
while (total <= 0):
    total = get_int("What is the total of purchase? ")

# Shipping calculation
if total <= 30:
    shipping_cost += 20
elif total <= 50:
    shipping_cost += 10
else:
    shipping_cost += 0

# Print calculation
print(f"Total cost: ${total}")
print(f"Shipping cost: ${shipping_cost}")
print("--------------------")
print(f"Grand total: ${total+shipping_cost}")

exit()
