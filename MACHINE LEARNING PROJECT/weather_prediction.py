import streamlit as st
import pandas as pd
from datetime import datetime

def load_data():
    return pd.read_csv("WEATHER.csv")

def get_weather_by_date(df, date):
    try:
        weather_data = df[df['Date'] == date]
        if weather_data.empty:
            return None
        return weather_data.iloc[0]
    except Exception as e:
        return None

def main():
    data = load_data()
    st.title("Weather Details by Date")
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Select", ["Show Weather Details"])

    if menu == "Show Weather Details":
        st.subheader("Show Weather Details")
        date_input = st.date_input("Enter a date")

        if st.button("Show Details"):
            # Convert date_input to string in 'MM/DD/YYYY' format
            date_input_str = date_input.strftime('%m/%d/%Y')

            # Convert 'Date' column in DataFrame to datetime objects for comparison
            data['Date'] = pd.to_datetime(data['Date'])

            # Convert date_input_str to datetime object for comparison
            date_input_dt = datetime.strptime(date_input_str, '%m/%d/%Y')

            weather_details = get_weather_by_date(data, date_input_dt)
            if weather_details is not None:
                st.write(f"Weather details for {date_input_str}:")
                st.write(f"Temperature at 9 AM: {weather_details['Temp9am']}")
                st.write(f"Temperature at 3 PM: {weather_details['Temp3pm']}")
                st.write(f"Minimum Temperature: {weather_details['MinTemp']}")
                st.write(f"Maximum Temperature: {weather_details['MaxTemp']}")
                st.write(f"Wind Speed at 9 AM: {weather_details['WindSpeed9am']}")
                st.write(f"Wind Speed at 3 PM: {weather_details['WindSpeed3pm']}")
                st.write(f"Humidity at 9 AM: {weather_details['Humidity9am']}")
                st.write(f"Humidity at 3 PM: {weather_details['Humidity3pm']}")
                st.write(f"Pressure at 9 AM: {weather_details['Pressure9am']}")
                st.write(f"Pressure at 3 PM: {weather_details['Pressure3pm']}")
                st.write(f"Cloud cover at 9 AM: {weather_details['Cloud9am']}")
                st.write(f"Cloud cover at 3 PM: {weather_details['Cloud3pm']}")
                st.write(f"Rainfall: {weather_details['Rainfall']}")
            else:
                st.write("No data available for the selected date.")

if __name__ == "__main__":
    main()