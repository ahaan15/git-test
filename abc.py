
row = 5

col = 3

mat = [['r', 'n', 'e'], ['r', 'n', 'n'], [
                                          
                                          'e', 'n', 'r'], ['n', 'n', 'e'], ['e', 'r', 'n']]

##mat = [['r', 'n', 'e'], ['r', 'n', 'e'], [

##   'e', 'e', 'n'], ['n', 'n', 'e'], ['e', 'r','n']]

newmat = None


def is_all_rotten(mat):
    
    for i in mat:
        
        for j in i:
            
            if j == 'n':
                
                return False

return True


def change_to_r(i, j):
    
    if mat[i][j] == 'n':
        
        mat[i][j] = 'r'


def ret_pos_of_r(mat, row, cols):
    
    ls = []
    
    for i in range(row):
        
        for j in range(cols):
            
            if mat[i][j] == 'r':
                
                ls.append([i, j])

return ls

def is_mat_changing(prevmat, newmat):
    
    for i in range(len(prevmat)):
        
        for j in range(len(prevmat[0])):
            
            if not prevmat[i][j] == newmat[i][j]:
                
                return True

return False


count = 0

flag = 0

while not is_all_rotten(mat):
    
    newmat = mat
        
        count += 1

for k in ret_pos_of_r(mat, row, col):
    
    i, j = k
        
        if mat[i][j] == 'r':
            
            try:
                
                change_to_r(i-1, j)
            
            except:
                
                pass
            
            try:
                
                change_to_r(i+1, j)
            
            except:
                
                pass
            
            try:
                
                change_to_r(i, j+1)
            
            except:
                
                pass
            
            try:
                
                change_to_r(i, j-1)
            
            except:
                
                pass

    if  is_mat_changing(mat, newmat):
        
        count = -1
            
            flag=1
            
            break

if flag==1:
    
    break

print(count)
