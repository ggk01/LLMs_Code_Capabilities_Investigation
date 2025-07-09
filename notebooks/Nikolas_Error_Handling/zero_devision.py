def calculate_percentage_change_from_start(data_series):
    first_value = data_series[0]
    return [((value - first_value) / first_value) * 100 for value in data_series]

data_series_failing = [0, 10, 20]
calculate_percentage_change_from_start(data_series_failing)