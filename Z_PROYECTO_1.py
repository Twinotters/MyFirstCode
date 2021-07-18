# Hacer un programa el cual consiga el peso de la gente y unidad y transformarla (libras y kilos)
weight = input('How much do you weight? ')
measurement = input('Is this value in kilograms or pounds? ')
answer_in_kilograms = 'kilograms'
answer_in_pounds = 'pounds'

if measurement.lower() == answer_in_kilograms:
    conversion = float(weight) * 2.02
    print(f"Your weight is {conversion} pounds")
elif measurement.lower() == answer_in_pounds:
    conversion_2 = float(weight) / 2.02
    print(f"Your weight is {conversion_2} kilograms ")

# se pone .lower para que lo que ponga el usuario sea del mismo formato que nuestras variables.
