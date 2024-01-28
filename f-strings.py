A way of string formatting.f-strings help us to place variables very conveinently in the strings.
Method-1
letter = "Hey my name is {} and I am from {}"
country="India"
name="Aarush"
print(letter.format(name,country))
Method-2
letter = "Hey I am {0} and I am from {1}"
name="Aarush"
country="India"
print(letter.format(name,country))
Method-3
name="Aarush"
country="India"
letter = f"Hey my name is {name} and I am from {country}")
print(letter)
Method-4
price=100.98383
print(f"This item costs {price:.2f}")
