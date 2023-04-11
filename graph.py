import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("login_data.csv")

# Assign unique alphabets to IP_Addres
ip_dict = {ip: chr(ord('a')+i) for i, ip in enumerate(df["IP_Addr"].unique())}
df["IP_Addr"] = df["IP_Addr"].apply(lambda x: ip_dict[x])

# Split the data into alerts and normal logins
alerts = df[df["Status"] == "alert"]
normal = df[df["Status"] == "normal"]

# Create the scatter plot
fig, ax = plt.subplots()
ax.scatter(alerts["Login_time"], alerts["IP_Addr"], color="red", label="Alert")
ax.scatter(normal["Login_time"], normal["IP_Addr"], color="green", label="Normal")

# Add axis labels and legend
ax.set_xlabel("Login_time")
ax.set_ylabel("IP_Addr")
# ax.legend()

# Show the plot
plt.show()
