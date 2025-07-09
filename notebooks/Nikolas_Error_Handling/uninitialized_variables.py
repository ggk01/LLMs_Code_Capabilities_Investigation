import csv

def execute_instructions():
    variables = {}
    with open('instructions.csv', newline='') as csvfile:
        reader = list(csv.DictReader(csvfile))
        i = 0
        while i < len(reader):
            row = reader[i]
            step = int(row['Step'])
            op = row['Operation']
            target = row['Target']
            value = row['Value']
            condition = row['Condition']

            def get_val(v):
                try:
                    return int(v)
                except ValueError:
                    return variables.get(v)

            if op == 'Set':
                variables[target] = get_val(value)

            elif op == 'Add':
                variables[target] = get_val(value) + get_val(condition)

            elif op == 'Subtract':
                variables[target] = get_val(value) - get_val(condition)

            elif op == 'Multiply':
                variables[target] = get_val(value) * get_val(condition)

            elif op == 'IfGreater':
                if get_val(target) > get_val(value):
                    i += 1  # execute next step
                else:
                    i += 2  # skip next step
                continue

            elif op == 'IfEqual':
                if get_val(target) == get_val(value):
                    i += 1  # execute next step
                else:
                    i += 2  # skip next step
                continue

            elif op == 'End':
                break

            i += 1

    print(variables)
execute_instructions()