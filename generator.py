import random
import csv

# Define the email, password, and IP_Addr lists for generating random data
ip_addresses = ["223.228.143.76", "10.0.0.1", "172.16.0.1", "223.228.143.76", "223.228.143.76"]

# Define the time ranges for generating random login times
time_ranges = [("06:00:00", "12:00:00"), ("18:00:00", "00:00:00"), ("00:00:00", "06:00:00")]

# Define the probability of a login attempt being an "alert"
alert_prob = 0.1

# Generate the data
data = []
for i in range(10000):
    email = "user1@gmail.com"
    password = "pass123"
    ip_address = random.choice(ip_addresses)
    login_time = random.randint(1, 24)
    if (ip_address != "223.228.143.76" and login_time not in [8, 9, 10, 11])  or random.random()<alert_prob:
        status = "alert"
    else:
        status = "normal"
    data.append([email, password, ip_address, login_time, status])

# Split the data into training and testing sets
# train_data = data[:4500]
# test_data = data[4500:]

# Write the data to a CSV file
with open("login_data_updated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Email", "Password", "IP_Addr", "Login_time", "Status"])
    writer.writerows(data)
