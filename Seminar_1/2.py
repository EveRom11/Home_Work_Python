# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def true():
    count=0
    result= True
    for X in True, False:
        for Y in True, False:
            for Z in True, False: 
                count+=1
                print(f"{count } {X= } {Y= } {Z= }   Result:{not(X or Y or Z)==(not X and not Y and not Z)}")
                
                
true()       