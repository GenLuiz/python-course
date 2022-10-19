temperature = 75
forecast = "rain"
raining = True

def stay_inside():
    print("Stay inside")

if temperature > 80:
    print("It's too hot")
    stay_inside()
elif temperature < 60:
    print("It's too cold")
    stay_inside()
elif not forecast == "rain":
    print("enjoy outdoors!")

if not raining:
    print("enjoy outdoors!")
else:
    print("it's raining")
    stay_inside()
print("Have a good day")