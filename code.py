# xyz = "Bob"
# print(f"Hello, {xyz}")

# xyz = "Bob"
# print("Hello {}".format(xyz))

x = 4863.4343091          # example float to format
# print(f"{x:.6}")          # f-string version
print("{:.6}".format(x))  # format method version
# output 4863.43

x = 4863.4343091

print("{:.3f}".format(x))   # 4863.434