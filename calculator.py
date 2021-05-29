

class Calculator:
    
    def return_sum(self, *args):

        return sum(args)
    
    def return_multiply(self, *args):

        multiply_result = 1

        for num in args:
            multiply_result *= num
        
        return multiply_result