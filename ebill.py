unit=int(input("How much unit u used for a month:"))
#meow meow meow meow meow meow meow meow meow
if unit<=100:
    print("Monthly electricity fees:",unit*5.56,"/-")
elif unit<300:
    print("Monthly electricity fees:",unit*12.4,"/-")
elif unit<500:
    print("Monthly electricity fees:",unit*16.63,"/-")
else:
    print("Monthly electricity fees:",unit*19.13,"/-")