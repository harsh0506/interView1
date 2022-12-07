import re

#regular expression
regex_seq = re.compile(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}")
#list of numbers
phone_list = ["2124567890", "212-456-7890", "(212)456-7890",
              "(212)-456-7890" , "212-456-7890" , "212.456.7890",
              "212 456 7890" , "+12124567890" ,"+12124567890",
              "+1 212.456.7890" , "+212-456-7890" , "1-212-456-7890","1-22-33-444-40"
              ]
#list of verified numbers
print( len( [x for x in phone_list if re.findall(regex_seq, x)]))
