def carPooling(trips, capacity):
    """
    :type trips: List[List[int]]
    :type capacity: int
    :rtype: bool
    """
    import collections
    drop_passengers = collections.defaultdict(int)
    pick_passengers = collections.defaultdict(int)
    final_location = -1
    for trip in trips:
        num_passengers, start, end = trip
        final_location = max(final_location, end)
        pick_passengers[start] += num_passengers
        drop_passengers[end] += num_passengers

    remaming_capacity = capacity
    for location in range(0, final_location + 1):
        if location in drop_passengers:
            remaming_capacity += drop_passengers[location]

        if location in pick_passengers:
            passenger_to_pick = pick_passengers[location]
            if remaming_capacity < passenger_to_pick:
                return False
            else:
                remaming_capacity -= pick_passengers[location]
    return True

trips = [[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]]
capacity = 23
print(carPooling(trips, capacity))
