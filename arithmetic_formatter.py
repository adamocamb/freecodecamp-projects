#This function accepts a list of problems and returns those problems formatted vertically and side-by-side. Answers are only displayed if show_answers=True.
def arithmetic_arranger(problems, show_answers=False):
    first_number_list = []
    second_number_list = []
    equals_list = []
    answer_list = []
    if len(problems) > 5: #Only accepts a max of 5 problems
            return 'Error: Too many problems.'
    else:        
        for expression in problems:
            expression_list = expression.split()
            #Only accepts addition and subtraction
            if '*' in expression or '/' in expression: 
                return "Error: Operator must be '+' or '-'."
                
            #Numbers must only contain digits
            elif not expression_list[0].isdigit() or not expression_list[2].isdigit():
                return 'Error: Numbers must only contain digits.'

            #Only accepts four digits per number
            elif len(expression_list[0]) > 4 or len(expression_list[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            #Format expression
            else:
                #get the width of the longest number in the expression
                width = max(len(expression_list[0]), len(expression_list[1]), len(expression_list[2]))
                #format first line
                first_number_list.append(expression_list[0].rjust(width + 6)) #add 6 to account for 4 spaces of padding and operator plus a space after
                #format second line
                second_number = expression_list[1] + expression_list[2].rjust(width + 1) #combine operator and second number into a string, with padding between equal to the width of the longest number plus an extra space after the operator
                second_number_list.append(second_number.rjust(width + 6)) #see formatting note for first_number_list
                #create equals line
                equals_line = ''.rjust(width + 2, '-')
                equals_list.append(equals_line.rjust(width + 6))
                #calculate answer and 
                if expression_list[1] == '+':
                    answer = int(expression_list[0]) + int(expression_list[2])
                    answer_list.append(str(answer).rjust(width + 6))
                elif expression_list[1] == '-':
                    answer = int(expression_list[0]) - int(expression_list[2])
                    answer_list.append(str(answer).rjust(width + 6))

    #format the first line of numbers
    new_first = first_number_list[0].strip().rjust(len(first_number_list[0])-4) #get rid of left side padding on first number
    first_number_list[0] = new_first #replace the first number with the newly formatted first number
    line_one = ''.join(first_number_list) #store the list as a string
    #print(line_one)
    #format the second line, same as above
    new_second = second_number_list[0].strip().rjust(len(second_number_list[0])-4)
    second_number_list[0] = new_second
    line_two = ''.join(second_number_list)
    #print(line_two)

    #format the third line (equals line)
    new_equals = equals_list[0].strip().rjust(len(equals_list[0])-4)
    equals_list[0] = new_equals
    line_three = ''.join(equals_list)
    #print(line_three)

    #format the fourth line, decide whether to show the answers
    first_answer = answer_list[0].strip().rjust(len(answer_list[0])-4)
    answer_list[0] = first_answer
    line_four = ''.join(answer_list)
    #print(line_four)
    
    #combine all four lines into one string with and without answers
    formatted_problems_answer = f'{line_one}\n{line_two}\n{line_three}\n{line_four}'
    formatted_problems = f'{line_one}\n{line_two}\n{line_three}'

    #only display the answers if show_answers is True
    if show_answers == True:
        return formatted_problems_answer
    else:
        return formatted_problems


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
