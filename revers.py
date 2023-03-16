def longest_palindrome(s):
    longest = 0

    for counter in range(1, len(s) + 1):
        for word in range(counter):
            text = s[word:counter]
            if text == text[::-1]:
                longest = max(longest, len(text))

    return longest


print(longest_palindrome("I like racecars that go fast"))