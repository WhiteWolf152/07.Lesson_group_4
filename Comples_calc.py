# Калькулятор комплексных чисел

# i^{2}=-1;\;i^{3}=-i;\;i^{4}=1;\;i^{5}=i и т. д.

# |z|={sqrt {(-1)^{2}+(-{sqrt {3}})^{2}}}={sqrt {1+3}}=2;

import math

text = "{sqrt {(-1)^{2}+(-{sqrt {3}})^{2}}}"

result = ""
for i in text:
    if i != " ":
        result += f"{i}"
    else:
        result += ""
    

list_of_math = result.split()
print(text)