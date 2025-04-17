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


