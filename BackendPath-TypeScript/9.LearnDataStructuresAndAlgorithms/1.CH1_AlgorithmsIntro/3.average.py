'''

We now need a way to show our LockedIn influencers the average follower count of the people they follow.
This will help them know if they're following people who are more or less popular than them.

Assignment
Complete the average_followers function. It should return the average of the given list of numbers.

If the list is empty, it should return None.

'''


def average_followers(nums):

    # Total sum variale
    total = 0

    # If array is empty return None
    if len(nums) == 0:
        return None

    # Iterate the array and sum all the numbers
    for num in nums:

        # Add to total
        total += num

    # Return the average
    return total/len(nums)
