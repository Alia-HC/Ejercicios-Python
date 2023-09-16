def factorial(num): 
    if num < 0: 
        print("No existe un factorial de un número negativo")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = 5; 

print("El factorial de ",num,"es", factorial(num))