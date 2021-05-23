class Solution:
    def numSubmat(self, mat):
        R, C = len(mat), len(mat[0])
        
        # precipitate mat to histogram
        for i in range(R):
            for j in range(C):
                if mat[i][j] and i > 0:
                    mat[i][j] += mat[i-1][j]
        
        ans = 0
        for i in range(R):
            stack = []
            cnt = 0
            for j in range(C): # We need to process each row at a time.
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    jj = stack.pop()
                    kk = stack[-1] if stack else -1
                    cnt -= (mat[i][jj] - mat[i][j]) * (jj - kk) # We are doing this because we want to get the mat[i][j]'s count
                    #The tricky part is when h[j-1] > h[j]. In this case, we need to "hypothetically" lower h[j-1] to h[j] to get an updated cnt*[j-1] before adding h[j] to get cnt[j].
                    
                cnt += mat[i][j] #  At column j, if h[j-1] <= h[j], it is apparent that cnt[j] = cnt[j-1] + h[j]. I think this is like a dp. cnt right now is the total count.
                ans += cnt
                stack.append(j)
        
        return ans