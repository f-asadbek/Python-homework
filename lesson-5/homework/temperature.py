cel = float(input("Enter a temperature in degrees F: "))

def convert_cel_to_far(cel):
    return (cel - 32) * 5/9

print(f"{cel} degrees F = {convert_cel_to_far(cel)}")

far = float(input("Enter a temperature in degrees C: "))

def convert_far_to_cel(far):
    return far * 9/5 + 32

print(f"{far} degrees C = {convert_far_to_cel(far)} degrees F")