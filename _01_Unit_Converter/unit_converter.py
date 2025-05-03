import streamlit as st

st.title("📊Unit Converter App ")
st.markdown("### It Converts Length, Temperature, Weight, and Time.")
st.write("Enter a value and select the conversion type and get the result.")

category = st.selectbox("Select a conversion type", ["Length", "Temperature", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value / 3.28084
        elif unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    if category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return value * 9/5 + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("📏Select a unit", ["Meters to feet","Feet to meters","Kilometers to miles", "Miles to kilometers"])
elif category == "Temperature":
    unit = st.selectbox("🌡️Select a unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
elif category == "Weight":
    unit = st.selectbox("⚖️Select a unit", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️Select a unit", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert ")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.write(f"The result is {result:.2f}")
