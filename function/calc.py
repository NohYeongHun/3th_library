def avg_calc(ratings):
    sum = 0
    for rating in ratings:
        sum += rating[0]

    avg = int(round(sum/len(ratings)))

    return avg 