class Sol:
    def transpose(self,matrix):
        print(*matrix)
        return list(zip(*matrix))

if __name__ == '__main__':
    p = Sol()
    print(p.transpose(matrix = [[1,2,3],[4,5,6]]))
