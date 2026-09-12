import config
conn = config.conn

print("Database connection established successfully.")

cursor = conn.cursor()
U_ssn = input("Enter your SSN : ")
cursor.execute("SELECT * FROM employee where ssn = %s;", (U_ssn,))
rows = cursor.fetchone()
print(rows)
# for row in rows:
#     print(row)

# df = pd.DataFrame(rows)
# df.to_csv("employee", index=False)
# print(df)

# conn.close()
# print("Database connection closed.")