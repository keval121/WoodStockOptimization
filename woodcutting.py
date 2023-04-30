def get_desired_lengths(desired):
    """
    Converts the desired board lengths to a dictionary
    with board length as key and desired frequency as value.
    """
    desired_lengths = {}
    for length, freq in desired:
        desired_lengths[length] = freq
    return desired_lengths

def get_current_lengths(inventory):
    """
    Converts the current inventory to a dictionary
    with board length as key and current frequency as value.
    """
    current_lengths = {}
    for length, freq in inventory:
        current_lengths[length] = freq
    return current_lengths

def row_waste_cut_pattern(lengths, frequency, board_length):
    """
    Returns a list of rows with their respective waste percentages,
    waste length, and cut frequency.
    """
    rows = []
    total_length = 0
    freq_arr = [0] * len(frequency)

    while freq_arr != frequency:
        curr_freq = [0] * len(frequency)

        for i, length in enumerate(lengths):
            if freq_arr[i] == frequency[i]:
                continue

            count = (board_length - total_length) // length

            if count == 0:
                continue

            if count > (frequency[i] - freq_arr[i]):
                curr_freq[i] = frequency[i] - freq_arr[i]
                total_length += length * curr_freq[i]
            else:
                curr_freq[i] = count
                total_length += length * count

        waste_length = board_length - total_length
        waste_percent = round(waste_length / board_length * 100, 2)
        rows.append([waste_percent, waste_length, curr_freq])

        for i, freq in enumerate(curr_freq):
            freq_arr[i] += freq

    return rows

def calculate_waste(inventory, desired, board_length):
    """
    Calculates the waste percentage for a given inventory,
    desired board lengths, and board length.
    """
    desired_lengths = get_desired_lengths(desired)
    current_lengths = get_current_lengths(inventory)
    lengths = []
    frequency = []

    for length, freq in current_lengths.items():
        if length in desired_lengths:
            lengths.append(length)
            frequency.append(min(freq, desired_lengths[length]))

    rows = row_waste_cut_pattern(lengths, frequency, board_length)
    num_boards = len(rows)
    total_waste = sum([row[1] for row in rows])
    total_length = num_boards * board_length
    waste_percent = round((1 - total_waste / total_length) * 100, 2)

    return num_boards, waste_percent

desired = [[40, 120], [24, 43], [5, 30], [12, 34], [10, 49], [5, 99], [10, 125], [26, 108], [26, 12], [10, 60]]
inventory = [[10, 50], [24, 20], [40, 5], [26, 5], [5, 100]]
board_length = 250

num_boards, waste_percent = calculate_waste(inventory, desired, board_length)
print(f"Number of boards: {num_boards}")
print(f"Waste percentage: {waste_percent}")
