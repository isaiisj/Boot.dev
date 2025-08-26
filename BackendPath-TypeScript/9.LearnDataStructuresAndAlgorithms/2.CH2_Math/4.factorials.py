'''

Assignment

Influencers need to be able to schedule posts to be published in the future.
We've found that the order in which the posts are published drastically affects their performance.

Complete the num_possible_orders function. 
It takes the number of posts an influencer has in their backlog as input and returns the total number
of possible orders in which we could publish the posts.

'''

def num_possible_orders(num_posts):

    # Start the counter in 0
    num_possible_orders = 1

    # Do a factorial calculation [ 1 * 2 ... * (n -1) * n]
    for i in range(num_posts):
        num_possible_orders  *= i+1;

    return num_possible_orders
