from datetime import datetime, timedelta

# 1. Get current day, month, year, hour, minute, timestamp
now = datetime.now()
print("1:")
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

# 2. Format current date
print("\n2:")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

# 3. Convert string to datetime
print("\n3:")
date_string = "5 December, 2019"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print("Converted datetime:", converted_date)

# 4. Time difference between now and New Year
print("\n4:")
new_year = datetime(now.year + 1, 1, 1)
time_diff = new_year - now
print("Time until New Year:", time_diff)

# 5. Time difference between 1 Jan 1970 and now
print("\n5:")
epoch = datetime(1970, 1, 1)
diff_since_epoch = now - epoch
print("Time since 1 Jan 1970:", diff_since_epoch)

# 6. Uses of datetime module
print("\n6:")
print("✅ Time series analysis")
print("✅ Timestamping user activity")
print("✅ Scheduling posts or events")
print("✅ Logging system events")
print("✅ Measuring execution time")