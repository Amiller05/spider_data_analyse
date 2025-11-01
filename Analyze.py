# anyyze the cost in the data/level_1 folders and go through the array of objects and add up the cost
# the cost is formatted as a decimal and at the dollar amount. Give me detailed analsys per page and the total cost.
import os
import json

def analyze_cost():
    for file in os.listdir('data/level_1'):
        with open(f'data/level_1/{file}', 'r') as f:
            data = json.load(f)
            # print(data)
            for item in data:
                total_cost = item['costs']['total_cost_formatted']
                print(f"Total cost for {item["url"]}: ${total_cost}")

analyze_cost()