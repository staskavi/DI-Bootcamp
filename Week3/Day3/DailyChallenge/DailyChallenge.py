secret_matrix = [ 
           [7, 'i', 'i'],
           ['T', 's', 'x'],
           ['h', '%', '?'],
           ['i','  ', '#'],
           ['s', 'M' ,' '],
           ['$', 'a' ,' '],
           ['#', 't', '%'],
           ['^', 'r', '!']
                           ]

def decrypt(matrix):
    decrypt_msg = ' '
    j = 0 
    matrix_range = range(len(matrix)-1)
    for i in matrix_range:
        if(j==len(matrix[0])):
           break
        column = [row[j] for row in matrix]
        for index in range(len(column)-1):
           column[index] = str(column[index])
           if(column[index].isalpha()):
             decrypt_msg+=column[index]
        j+=1
    print(decrypt_msg)   

decrypt(secret_matrix)         

        