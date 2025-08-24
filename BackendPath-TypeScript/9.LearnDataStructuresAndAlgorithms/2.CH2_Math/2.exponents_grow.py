'''

While the influencers who use our platform are really great at taking selfies,
most aren't super great at math. We need to write a tool that predicts an influencer's
follower growth over time.

Complete the get_follower_prediction function. It takes a follower_count integer,
a influencer_type string and a num_months integer, and returns an integer.

Calculate the number of followers an influencer will have after however many months according to the influencer type:

"fitness": follower count quadruples each month
"cosmetic": follower count triples each month
other: follower count doubles each month

For example, if a "fitness" influencer starts with 10 followers, then after 1 month they would have 40 followers.
After 2 months, they would have 160 followers, and so on.

Use the following geometric sequence formula that's slightly modified for this problem:

total = a1 * r^n

'''

def get_follower_prediction(follower_count, influencer_type, num_months):


    # Number of growing
    number_of_growing = 0

    # Assign number of growing depending on influencer type
    if influencer_type == "fitness":
        number_of_growing = 4
    elif influencer_type == "cosmetic":
        number_of_growing = 3
    else:
        number_of_growing = 2

    # Total variable
    total = follower_count * (number_of_growing ** num_months)

    return total

