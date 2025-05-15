# Given an array of strings words and an integer k, return the k most frequent strings.Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
def topKFrequent(words,k):
    freq={}
    for word in words:
        freq[word]=freq.get(word,0)+1
    sorted_freq=sorted(freq.items(),key=lambda x:(-x[1],x[0]))
    # freq.items() will give us the key value pairs like (i,2),(love,2),(leetcode,1),(coding,1)
    # Then we will sort it based on the values and then we will return the keys
    # -x[1],x[0]) means that we will sort it based on the values in descending order and then we will sort it based on the keys in ascending order

    result=[word for word,_ in sorted_freq[:k]]
    # freq[:k] gets the first k elements of the sorted list.
    return result
words = ["i","love","leetcode","i","love","coding"]
k = 2
print(topKFrequent(words,k))

# kth pair with smallest sum
# kth smallest elemnt insortred matrix
