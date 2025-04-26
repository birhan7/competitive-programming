class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(img)):
            temp = []
            for j in range(len(img[i])):
                sum = img[i][j]
                count = 1
                if i - 1 >= 0 and j - 1 >= 0:
                    sum += img[i-1][j-1] + img[i-1][j] + img[i][j-1]
                    count += 3
                elif i - 1 >= 0:
                    sum += img[i-1][j]
                    count += 1
                elif j - 1 >= 0:
                    sum += img[i][j-1]
                    count += 1

                if i + 1 < len(img) and j + 1 < len(img[i]):
                    sum += img[i+1][j+1] + img[i+1][j] + img[i][j+1]
                    count += 3
                elif i + 1 < len(img):
                    sum += img[i+1][j]
                    count += 1
                elif j + 1 < len(img[i]):
                    sum += img[i][j+1]
                    count += 1

                if  j + 1 < len(img[i]) and i - 1 >= 0:
                    sum += img[i-1][j+1]
                    count += 1
                if j - 1 >= 0 and i + 1 < len(img):
                    sum += img[i+1][j-1]
                    count += 1

                temp.append(sum//count)
            ans.append(temp)
        return ans
                

        