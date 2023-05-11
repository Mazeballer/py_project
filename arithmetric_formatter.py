def arithmetic_arranger(problems, solve = True):
# first section--------------------------------------------------------------------------------------------------------
  
  problems_group = []
  solution_list = []
  problems_layout = []
  final_solution_with_space = []
  a = "\n"
  
  # add solution list
  
  for group in range(len(problems)):
    solutions = str(eval(problems[group]))
    solution_list.append(solutions)
  
  # make sure that number of problem does not exceeds 4.
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # to make sure only "+" and "-" exists.
  
  for line in range(len(problems)):
    if "+" in problems[line]:
      pass
    elif "-" in problems[line]:
      pass
    else :
      return "Error: Operator must be '+' or '-'."

  # to split the string
  
  for line in range(len(problems)):
    problems[line] = problems[line].split(" ")
    problems_group.append(problems[line])
  
  # to check whether the string is a digit or not.
  
  for group in range(len(problems)):
    if problems_group[group][0].isdigit() == False:
      return "Error: Numbers must only contain digits." 
    elif problems_group[group][2].isdigit() == False:
      return "Error: Numbers must only contain digits."
    
  # make sure that lenght of number does not exceeds 4.
  
  for group in range(len(problems)):
    if len(problems_group[group][0]) > 4 :
      return "Error: Numbers cannot be more than four digits."
    elif len(problems_group[group][1]) > 4 :
      return "Error: Numbers cannot be more than four digits."

# second section------------------------------------------------------------------------------------------------------------------   
  
  # to create the layout of the problems.
  
  for charac in range(len(problems)):
    if len(problems_group[charac][0]) < len(problems_group[charac][2]):
      total_space = len(problems_group[charac][2]) + 2
      top = " " * (total_space - len(problems_group[charac][0])) + problems_group[charac][0]
      middle = problems_group[charac][1] + " " +  problems_group[charac][2]
      dash = "-" * total_space
      sol_line = " " * (total_space - len(str(solution_list[charac]))) + str(solution_list[charac])
      final_solution_with_space.append(sol_line)
      problem = f'{top}\n{middle}\n{dash}'
      problems_layout.append(problem)
      
    if len(problems_group[charac][0]) == len(problems_group[charac][2]):
      total_space = len(problems_group[charac][2]) + 2
      top = " " * (total_space - len(problems_group[charac][0])) + problems_group[charac][0]
      middle = problems_group[charac][1] + " " +  problems_group[charac][2]
      dash = "-" * total_space
      sol_line = " " * (total_space - len(str(solution_list[charac]))) + str(solution_list[charac])
      final_solution_with_space.append(sol_line)
      problem = f'{top}\n{middle}\n{dash}'
      problems_layout.append(problem)
      
    if len(problems_group[charac][0]) > len(problems_group[charac][2]):
      total_space = len(problems_group[charac][0]) + 2
      top = "  " + problems_group[charac][0]
      middle = problems_group[charac][1] + " " * (total_space - (len(problems_group[charac][2])+1)) + problems_group[charac][2]
      dash = "-" * total_space
      sol_line = " " * (total_space - len(str(solution_list[charac]))) + str(solution_list[charac])
      final_solution_with_space.append(sol_line)
      problem = f'{top}\n{middle}\n{dash}'
      problems_layout.append(problem)

# third section-------------------------------------------------------------------------------------------------------

  # only questions(without answer)
  
  if solve == False:
    lines = a.join(problems_layout).split('\n')  # Split the string into separate lines
    operands = []
    operators = []
    dash = []

    for line in lines:
      line = line.rstrip()  # Remove leading/trailing whitespace
      if line.startswith("--"):
        dash.append(line)  # Store the dash lines
      elif line.startswith('-') or line.startswith("+"):
        operators.append(line)  # Store the horizontal separator lines
      else:
        operands.append(line)
  
    horizontal_dash = '    '.join(dash)
    horizontal_operands = '    '.join(operands)
    horizontal_operators = '    '.join(operators)
  
    horizontal_addition =  horizontal_operands + '\n' + horizontal_operators + '\n' + horizontal_dash
    arranged_problem =  horizontal_addition  
  
  # questions(with answer)
  
  if solve == True:
    lines = a.join(problems_layout).split('\n')  # Split the string into separate lines
    operands = []
    operators = []
    dash = []

    for line in lines:
      line = line.rstrip()  # Remove leading/trailing whitespace
      if line.startswith("--"):
        dash.append(line)  # Store the dash lines
      elif line.startswith('-') or line.startswith("+"):
        operators.append(line)  # Store the horizontal separator lines
      else :
        operands.append(line)
  
    horizontal_dash = '    '.join(dash)
    horizontal_operands = '    '.join(operands)
    horizontal_operators = '    '.join(operators)
    horizontal_solution = '    '.join(final_solution_with_space)
  
    horizontal_addition =  horizontal_operands + '\n' + horizontal_operators + '\n' + horizontal_dash + '\n' + horizontal_solution
    arranged_problem =  horizontal_addition  
  
  return arranged_problem

print(arithmetic_arranger(["32 + 1799", "3801 - 2", "45 + 43", "123 + 49"]))
    
    
    

