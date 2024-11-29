print("the Love Calculator is calculating your score...")
name1 = input("Enter the name for the first preson") # What is your name?
name2 = input("enter the name for the second person") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name =  name1+name2
in_lower_case = combined_name.lower()
t=in_lower_case.count('t')
r=in_lower_case.count('r')
u=in_lower_case.count('u')
e=in_lower_case.count('e')
first_digit=t+r+u+e

l=in_lower_case.count('l')
o=in_lower_case.count('o')
v=in_lower_case.count('v')
e=in_lower_case.count('e')
second_digit = l+o+v+e

score= str(first_digit) + str(second_digit)

if int(score)<10 or int(score)>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score)>40 and int(score)<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
"""

                      _..-'(                       )`-.._
                   ./'. '||\\.       (\_/)       .//||` .`\.
                ./'.|'.'||||\\|..    )O O(    ..|//||||`.`|.`\.
             ./'..|'.|| |||||\`````` '`"'` ''''''/||||| ||.`|..`\.
           ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.
          /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`\
         '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
        '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`       ascii.co.uk
        |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|        ascii art
        V    V         V          }' `\ /' `{          V         V    V
        `    `         `               V               '         '    '

        """