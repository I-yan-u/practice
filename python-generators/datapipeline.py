file = 'python-generators/techcrunch.csv'
lines = (line for line in open(file))
clean_lines = (line.rstrip().split(',') for line in lines)
cols = next(clean_lines)
data_dict = (dict(zip(cols, data)) for data in clean_lines)
filtered_raised_amt = (
    int(data['raisedAmt'])
    for data in data_dict
    if data['round'] == 'a'
)

print(sum(filtered_raised_amt))