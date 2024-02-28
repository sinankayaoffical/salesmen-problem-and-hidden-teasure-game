import sys

def salesman_problem_dp(distances):
    """
    Finds the shortest route using dynamic programming.

    Args:
        distances: A dictionary of distances between city pairs.

    Returns:
        A tuple containing the optimal route and the total distance.
    """

    n = len(distances)  # Number of cities
    # Create a DP table to store minimum distances and parent nodes
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[None] * n for _ in range(1 << n)]

    # Base case: Start from any city and visit no other city yet
    for i in range(n):
        dp[1 << i][i] = 0

    # Iterate over subsets of visited cities (using bitmask)
    for subset in range(2, 1 << n):
        for i in range(n):
            # Check if the current city is included in the subset
            if subset & (1 << i) > 0:
                # Explore all possible previous cities by removing them from the subset
                for j in range(n):
                    if i != j and (subset & (1 << j)) > 0:
                        # Update minimum distance and parent node
                        new_dist = dp[subset ^ (1 << i)][j] + distances[(i, j)]
                        if new_dist < dp[subset][i]:
                            dp[subset][i] = new_dist
                            parent[subset][i] = j

    # Reconstruct the optimal route from final state
    route = []
    end_city = 0  # Can be any starting city
    current_city = end_city
    visited = 2**n - 1

    while visited > 0:
        route.append(current_city)
        prev_city = parent[visited][current_city]
        visited ^= 1 << current_city
        current_city = prev_city

    route.append(end_city)
    route.reverse()  # Reverse to get the starting order

    return route, dp[(1 << n) - 1][end_city]

# Example usage
distances = {
    ('a', 'b'): 10,
    ('a', 'c'): 19,
    ('a', 'd'): 22,
    ('a', 'e'): 5,
    ('a', 'f'): 12,
    ('b', 'c'): 7,
    ('b', 'd'): 3,
    ('b', 'e'): 9,
    ('b', 'f'): 15,
    ('c', 'd'): 8,
    ('c', 'e'): 16,
    ('c', 'f'): 2,
    ('d', 'e'): 4,
    ('d', 'f'): 1,
    ('e', 'f'): 11,
}

optimal_route, total_distance = salesman_problem_dp(distances)
print("Optimal Route:", optimal_route)
print("Total Distance:", total_distance)
