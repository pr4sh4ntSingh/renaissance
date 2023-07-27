class Solution:
    """ Dynamic Programming, Medium, ACCEPTED Solution
    ---------------------------------------------------------------------------
    Algorithm:
        palindrom(s[i:j]) will be panidrome if 
                        s[i+1:j-1] is a palindrome 
                        and s[i] == s[j]
    
    Example- s = "a{---}a" so s will be panlindrome only if {---} is already a 
                palindrome and fist and last digit is equal.
                
    ---------------------------------------------------------------------------
    Data Structure:
        table- matrix of size (n*n)
               where value table[i][j] is nonzero if s[i:j] is not a palindrom.
                                       or zero [if not a palindrome.]
            
    """

    def longestPalindrome(self, s: str) -> str:
        #s = "aabdababababababbbabbabab"
        s_len = len(s)
        m = range(len(s))

        # populate table diognals are 1, others are 0.
        # if table[i,j] = 1 it means s[i:j] is a palindrome.
        table = [[1 if i == j else 0 for j in m] for i in m]

        # Fill all 2 length strings
        # String of length 2 are palindrome only and only if both the chars are
        # same.
        for i in range(s_len-1):
            i, j = i, i+1
            table[i][j] = 2 if s[i] == s[j] else 0

        # Now fill all other values in matrix
        # because length 1 and length 2 substrings are already polpulated
        # Note that you have to move length-size. You can not move row or col-
        # wise. Because to decide on length(3) palindrome you will need palidrom
        # status of length(2) strings.
        # See wrong implementation in last of this code.
        for substring_length in range(2, s_len):

            for i in range(0, s_len-substring_length):  # imp for index error
                j = i + substring_length

                # if substring s[i+1:j-1] is palindrome and s[i]==s[j]
                if table[i+1][j-1] != 0 and s[i] == s[j]:
                    #print(s[i:j+1]+" Y --checked via "+s[i+1:j])

                    table[i][j] = substring_length+1
                else:
                    table[i][j] = 0
                    #print(s[i:j+1]+" N --checked via "+s[i+1:j])

        #print(list(s))
        i,j = self.find_max_index(table)
        return(s[i:j+1])
        
    def find_max_index(self, table):
        max_value = -1
        max_indices = (-1,-1)
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i][j] > max_value:
                    max_value = table[i][j]
                    max_indices = (i,j)
        return max_indices
    
    
    
""" Wrong - Just for analysis purpose.

        # Now fill all other values in matrix

        for i in range(s_len):
            # because length 1 and length 2 substrings are already polpulated
            for j in range(i+2, s_len):

                # if substring s[i+1:j-1] is palindrome and s[i]==s[j]
                if table[i+1][j-1] != 0 and s[i] == s[j]:
                    print(s[i:j+1]+" +1 --checked for "+s[i+1:j])

                    table[i][j] = table[i+1][j-1] + 2
                else:
                    table[i][j] = 0
                    print(s[i:j+1]+" -0 --checked for "+s[i+1:j])

"""