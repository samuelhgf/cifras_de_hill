matrix_length = int(input("Digite o tamanho da matriz: "))

code_matrix = []

alfabeto = ['Z']
for x in range(65, 90):
    alfabeto.append(chr(x))

for i in range(matrix_length):
    code_matrix.append(list(map(int, input("Digite a linha %d separada por espaços entre os numeros: " % (i+1)).split(" "))))

original_message = input("Digite a mensagem original: ").upper()

if (len(original_message) > matrix_length):
    while(len(original_message) % matrix_length != 0):
          original_message += original_message[len(original_message) - 1]
elif(len(original_message) < matrix_length):
    while(matrix_length % len(original_message) != 0):
          original_message += original_message[len(original_message) - 1]

message_map = []                                         

counter = 0
for i in range(int(len(original_message) / matrix_length)):
    column = []
    for i in range(matrix_length):
        column.append(alfabeto.index(original_message[counter]))
        counter += 1
        
    message_map.append(column)

matrix_num_crip = []

cripted_message = ""

line_counter = 0
for i in range(int(len(original_message) / matrix_length)):
    result_column = []
    for line in code_matrix:
        sum_element_with_letter = 0
        element_counter = 0
        for element in line:
            sum_element_with_letter += (element * message_map[line_counter][element_counter])
            element_counter += 1

        cripted_message += alfabeto[sum_element_with_letter % 26]

    line_counter += 1
    matrix_num_crip.append(result_column)


print(cripted_message)
