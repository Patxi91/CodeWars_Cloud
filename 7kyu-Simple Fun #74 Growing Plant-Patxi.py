def growing_plant(up_speed, down_speed, desired_height):
    height = 0
    days = 0

    while height < desired_height:
        days += 1
        height += up_speed

        if height >= desired_height:
            break

        height -= down_speed

    if desired_height == 0 and days == 0:
        return 1
    else:
        return days
