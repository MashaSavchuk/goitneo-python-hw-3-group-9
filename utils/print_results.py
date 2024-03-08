def print_results(birthdays_per_week):
    if len(birthdays_per_week):
        result = ''
        for day, names in birthdays_per_week.items():
            result += f"{day}: {','.join(names)}\n"
        return result
