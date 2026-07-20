def longestUniqueSubstr(s):
    n = len(s)
    res = 0

    for i in range(n):

        # Initializing all characters as not visited
        vis = [False] * 26

        for j in range(i, n):

            # If current character is visited
            # Break the loop
            if vis[ord(s[j]) - ord('a')] == True:
                break

            # Else update the result if this window is larger,
            # and mark current character as visited.
            else:
                res = max(res, j - i + 1)
                vis[ord(s[j]) - ord('a')] = True
    return res
  

if __name__ == "__main__":
    s = "geeksforgeeks"
    print(longestUniqueSubstr(s))