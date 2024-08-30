def arithmetic_arranger(problems, show_answers=False):
  try: 

      if len(problems) > 5:
          raise ValueError('Error: Too many problems.')

      #declare variables for results
      top = ""
      bottoms = ""
      equals = ""
      answers = ""
      spacer = "    "

      for problem in problems:
          elements = problem.split()

          #limit operator to '+' and '-'
          if elements[1] not in ['+','-']:
              raise ValueError("Error: Operator must be '+' or '-'.")

          #each number must be a digit
          if not elements[0].isnumeric() or not elements[2].isnumeric():
              raise ValueError("Error: Numbers must only contain digits.")

          #each number must be <= 4 digits
          if len(elements[0]) > 4 or len(elements[2]) > 4:
              raise ValueError('Error: Numbers cannot be more than four digits.')

          # maxLen = max(list(map(lambda val: len(val), elements))) + 2
          maxLen = max((len(val) for val in elements)) + 2
          print("maxLen", maxLen)

          top = top + elements[0].rjust(maxLen) + spacer
          bottom = elements[1] + elements[2].rjust(maxLen-1) 
          bottoms = bottoms + bottom.rjust(maxLen) + spacer
          equal = "-"
          equals = equals + equal.rjust(maxLen,'-') + spacer

          if show_answers is True:
              if elements[1] == '+':
                  answer = int(elements[0]) + int(elements[2])
              else:
                  answer = int(elements[0]) - int(elements[2])

              answers = answers + str(answer).rjust(maxLen) + spacer

      result = top.rstrip() + "\n" + bottoms.rstrip() + "\n" + equals.rstrip()
      if show_answers is True:
          result = result + "\n" + answers.rstrip()

      return result
  except ValueError as e:
      return str(e)

problem = ["3 + 855", "988 + 40"]

print(f'\n{arithmetic_arranger(problem, True)}\n')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}\n')