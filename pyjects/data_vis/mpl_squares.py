import matplotlib.pyplot as plt

input_val = []
squares = []

for num in range(0, 1001):
    input_val.append(num)
    squares.append(num**2)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# ax.scatter(input_val, squares, color='red', s=20)
# ax.scatter(input_val, squares, color=(0, .8, 0), s=20)
ax.scatter(input_val, squares, c=squares, cmap=plt.cm.Blues, s=20)
ax.axis([0, 1100, 0, 1_100_000])

# Set labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

ax.tick_params(labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()