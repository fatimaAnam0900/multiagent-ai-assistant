from tools import weather_tool

response = weather_tool.invoke({"location": "Lahore"})
print(response)