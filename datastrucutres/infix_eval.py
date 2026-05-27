import stack
precedences = {"+":1,"-":1,"*":2,"/":2,")":0,"(":0}
def infix_eval(expression):
    operators = stack.Stack()
    operands = stack.Stack()
    items = expression.split(" ")
    operators.append("(")
    for i in items:
        if i in ["*","/","+","-",")","("]:
            operate(operators,operands,i)
        else:
            operands.append(float(i))
        #print(operands)
        #print(operators)
    operate(operators,operands,")")
    ans = operands.pop()
    print(expression+" = "+str(ans))
    return ans

def operate(operators,operands,operator):
    if operands.numItems <2:
        operators.append(operator)
        return
    else:
        if operator == "(":
            operators.append("(")
            return
        topOp = operators.pop()
        while operands.numItems > 1 and precedences[topOp]>= precedences[operator]:
            if operator == ")" and topOp == "(":
                return
            else:
                b = operands.pop()
                a = operands.pop()
                if topOp == "+":
                    operands.append(a+b)
                if topOp == "-":
                    operands.append(a-b)
                if topOp == "*":
                    operands.append(a*b)
                if topOp == "/":
                    operands.append(a/b)
                topOp = operators.pop()
        operators.append(topOp)
        operators.append(operator)
def infix_test():
    ans1 = infix_eval("( 6 + 5 ) * 4 - 9")
    ans2 = infix_eval("2 + 3 * 1 + 2")
    ans3 = infix_eval("3.65 + 2 * ( 7 + ( 2 * 4 ) )")
    if ans1 == 35 and ans2 == 7 and ans3 == 33.65:
        print("It works")
    else:
        print("It still needs work")
    
if __name__ == "__main__":
    infix_test()