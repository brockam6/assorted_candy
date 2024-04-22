import plotly.express as px

from yahtzee import Yahtzee

yahtz = Yahtzee()
poss_results = [yahtz.oak3, yahtz.oak4, yahtz.yahtzee, yahtz.small_s, yahtz.large_s, yahtz.nothing]
results = []
rolls = 1000

[results.append(yahtz.interpret_results(yahtz.roll_em())) for i in range(rolls)]

print(f"{results}")

# Analyze results
frequencies = []

[frequencies.append(results.count(val)) for val in poss_results]

title = f"Odds of rolling each lower category in Yahtzee based on {rolls} attempts"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()