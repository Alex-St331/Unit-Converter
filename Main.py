import tkinter as tk
from tkinter import ttk

# Conversion constants
MILES_IN_KM = 0.621371
FEET_IN_METER = 3.28084
INCHES_IN_CM = 0.393701
POUNDS_IN_KG = 2.20462
POUNDS_IN_G = 0.00220462
CM_IN_INCHES = 2.54
KG_IN_POUNDS = 0.453592
G_IN_POUNDS = 0.00220462

def convert_units():
    input_value = float(input_entry.get())
    input_unit = input_unit_combobox.get()
    output_unit = output_unit_combobox.get()

    # Set a default value for conversion_factor
    conversion_factor = None

    # Perform the appropriate conversion
    if input_unit == 'Kilometers' and output_unit == 'Miles':
        conversion_factor = MILES_IN_KM
    elif input_unit == 'Meters' and output_unit == 'Feet':
        conversion_factor = FEET_IN_METER
    elif input_unit == 'Centimeters' and output_unit == 'Inches':
        conversion_factor = INCHES_IN_CM
    elif input_unit == 'Inches' and output_unit == 'Centimeters':
        conversion_factor = CM_IN_INCHES
    elif input_unit == 'Kilograms' and output_unit == 'Pounds':
        conversion_factor = POUNDS_IN_KG
    elif input_unit == 'Pounds' and output_unit == 'Kilograms':
        conversion_factor = KG_IN_POUNDS
    elif input_unit == 'Grams' and output_unit == 'Pounds':
        conversion_factor = POUNDS_IN_G
    elif input_unit == 'Pounds' and output_unit == 'Grams':
        conversion_factor = G_IN_POUNDS

    if conversion_factor is None:
        output_label['text'] = "Invalid unit combination"
    else:
        output_value = input_value * conversion_factor
        output_label['text'] = output_value

    output_value = input_value * conversion_factor
    output_label['text'] = output_value

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create the input value entry
input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1)

# Create the input unit combobox
input_unit_combobox = ttk.Combobox(root, values=['Kilometers', 'Meters', 'Centimeters', 'Inches', 'Kilograms', 'Pounds', 'Grams'])
input_unit_combobox.grid(row=0, column=2)

# Create the output unit combobox
output_unit_combobox = ttk.Combobox(root, values=['Miles', 'Feet', 'Inches', 'Centimeters', 'Pounds', 'Kilograms', 'Grams'])
output_unit_combobox.grid(row=1, column=2)

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.grid(row=2, column=1, columnspan=2)

# Create the output label
output_label = tk.Label(root, text="")
output_label.grid(row=3, column=1, columnspan=2)

# Start the main loop
root.mainloop()
