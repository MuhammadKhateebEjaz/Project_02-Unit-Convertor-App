import streamlit as st

st.title=("🌍unit Converter App")
st.markdown("### Converts Length, Weigth and Time Instantly.")
st.write("Wellcome! Select a categeory, enter a value and het the converted result in real-time :")

category = st.selectbox("Choser  a Categoty", ["Length", "Weight", "Time"])

def convert_units(category, value):
    if category == "Length":
if unit == "kilometer to miles":

      return value * 0.621371


    elif unit == "miles to kilometer":
        return value / 0.621371



elif category == "Weight":
    if unit == "kilogram to pound":
        return value * 2.20462


    elif unit == "pound to kilogram":
        return value / 2.20462
    
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
        return value / 60
    
        
    elif unit == "Hours to  minutes":
        return value * 60
 
 elif unit == "Hours to days":
        return value / 24
    elif unit == "days to hours":
        return value * 24

return 0

if category == "Length":
     Unit = st.selectbox("🗞 Select Conversation", [" Miles in Kilometer", "kilometer to miles"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversation", ["kilograms to pounds", "pounds to kilogram"])

elif category == "Time":
    unit = st.selectbox("⏳ Select Conversation", ["Seconds to minutes", "minutes to seconds", "minutes to hours", "Hours to  minutes", "Hours to days", "days to hours"])

    value = st.number_input("Enter the value to convert")


    if st.button("Convert"):
        if value:
            converted_value = convert_units(category, value unit)
            st.success(f"The Result is : {reslult:.2f}")
        else:
            st.error("❗ Please enter a valid number.")





# import streamlit as st

# # Streamlit App Title
# st.title("Google Unit Converter - Streamlit")

# # Unit categories
# categories = {
#     "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
#     "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274},
#     "Temperature": {"Celsius": 1, "Fahrenheit": "temp_f", "Kelvin": "temp_k"},
# }

# # Select unit category
# category = st.selectbox("Select a category", list(categories.keys()))

# # Select from and to units
# from_unit = st.selectbox("From", list(categories[category].keys()))
# to_unit = st.selectbox("To", list(categories[category].keys()))

# # Get user input value
# value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# # Conversion logic
# def convert(value, from_unit, to_unit, category):
#     if category == "Temperature":
#         if from_unit == "Celsius" and to_unit == "Fahrenheit":
#             return (value * 9/5) + 32
#         elif from_unit == "Celsius" and to_unit == "Kelvin":
#             return value + 273.15
#         elif from_unit == "Fahrenheit" and to_unit == "Celsius":
#             return (value - 32) * 5/9
#         elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
#             return (value - 32) * 5/9 + 273.15
#         elif from_unit == "Kelvin" and to_unit == "Celsius":
#             return value - 273.15
#         elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
#             return (value - 273.15) * 9/5 + 32
#         return value
#     else:
#         return value * (categories[category][to_unit] / categories[category][from_unit])

# # Convert button
# if st.button("Convert"):
#     result = convert(value, from_unit, to_unit, category)
#     st.success(f"Converted Value: {result:.2f} {to_unit}")










