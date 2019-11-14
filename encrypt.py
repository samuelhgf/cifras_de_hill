matrix_length = int(input("Digite o tamanho da matriz: "))

code_matrix = [] #The matrix of the code that will be used to encrypt
message_map = [] #The matrix of the number of each letter in the original message
encrypted_message = "" #The encrypted message

#Creates the alphabet with the index iquals to the letter nuber according Hill-s Ciffer
alphabet = ['Z']
for x in range(65, 90):
    alphabet.append(chr(x))

#Populates the code_matrix with a list contains the numbers of each line
for i in range(matrix_length):
    code_matrix.append(
        list(map(int, input("Digite a linha %d separada por espaços entre os numeros: " % (i + 1)).split(" "))))

#Ask the user to input the original message and parses it to UPPERCASE
original_message = input("Digite a mensagem original: ").upper()

#Make the original message multiple of the code matrix size
if len(original_message) > matrix_length:
    while len(original_message) % matrix_length != 0:
        original_message += original_message[len(original_message) - 1]
elif len(original_message) < matrix_length:
    while matrix_length % len(original_message) != 0:
        original_message += original_message[len(original_message) - 1]

#Separetes as a matrix with the number of each letter according the alphabet created previously
counter = 0
for i in range(int(len(original_message) / matrix_length)):
    column = []
    for j in range(matrix_length):
        column.append(alphabet.index(original_message[counter]))
        counter += 1

    message_map.append(column)

#Makes the encrypted message using each line of the code and each list in the message_map as a multiplication of matrix
line_counter = 0
for i in range(int(len(original_message) / matrix_length)):
    for line in code_matrix:
        sum_element_with_letter = 0
        element_counter = 0
        for element in line:
            sum_element_with_letter += (element * message_map[line_counter][element_counter])
            element_counter += 1

        encrypted_message += alphabet[sum_element_with_letter % 26]

    line_counter += 1

#Shows the encrypted message to the user
print(encrypted_message)
