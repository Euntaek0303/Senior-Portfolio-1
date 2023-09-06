print("Welcome to the Space Travel Calculator")

distance = input("Hello, please enter the distance it takes to reach the your destination in light years")

speed = input("Please enter the speed of your spacecraft (in fraction of the speed of light)")

time = int(distance)/int(speed)

print("It will take you", time , "years to reach your destination")