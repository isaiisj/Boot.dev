def get_estimated_spread(audiences_followers):

    # Accumulator for sum of audience followers
    sum_audience_followers = 0

    # Total number of follower the list
    number_of_followers = len(audiences_followers)

    # Check if list is not empty
    if number_of_followers == 0:
        return 0

    # Iterate the list
    for follower in audiences_followers:
        sum_audience_followers += follower

    # Get the average audience follower
    average_audience_followers = sum_audience_followers/number_of_followers

    # Calculate estimated spread
    estimated_spread = average_audience_followers * (number_of_followers ** 1.2)

    return estimated_spread
