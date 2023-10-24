def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None

    students = 0

    for hours in permanence_period:
        if not (isinstance(hours[0], int) and isinstance(hours[1], int)):
            return None
        if target_time >= hours[0] and target_time <= hours[1]:
            students += 1
    return students
