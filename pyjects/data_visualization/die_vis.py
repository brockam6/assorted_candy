import plotly.express as px

from die import Die

die = Die()
die2 = Die()

results = []
rolls = 1000

[results.append(die.roll() + die2.roll()) for num in range(rolls)]

# Analyze results
frequencies = []
max_result = die.num_sides + die2.num_sides
poss_results = range(2, max_result + 1)

[frequencies.append(results.count(val)) for val in poss_results]

title = f"Results of rolling 2 D6 {rolls} times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update(xaxis_dtick=1)
fig.show()