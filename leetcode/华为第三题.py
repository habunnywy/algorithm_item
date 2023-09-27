import re

class Calculator:
    def __init__(self):
        self.variables={}

    def evalute(self,expression):
        if expression.startswith('let'):
            parts=expression[3:].strip().split('=')
            if len(parts)!=2:
                return "<syntax-error>"
            var_name,expr=parts
            var_name=var_name.strip()
            if not re.match('^[a-zA-Z_][a-zA-Z0-9_]*$',var_name):
                return '<syntax-error>'

            value=self.parse(expr.strip())
            if value=='<syntax-error>' or value == '<undefined>' or value in ['<underflow>','<overflow>']:
                return value
            self.variables[var_name]=value
            return None
        elif expression.startswith('out'):
            var_name=expression[3:].strip().strip('()')
            return self.variables.get(var_name,'<underfined>')
        else:
            return '<syntax-error>'

    def parse(self,expr):
        tokens=re.split('([+\-*/])',expr)
        if len(tokens)==1:
            if tokens[0].isdigit() or (tokens[0][0]=='-' and tokens[0][1:].isdigit()):
                return int(tokens[0])
            return self.variables.get(tokens[0],'<underfined>')

        left =self.parse(tokens[0].strip())

        if left in ['<syntax-error>','<underfined>','<underflow>','<overflow>']:
            return left
        for i in range(1,len(tokens),2):
            op=tokens[i]
            right=self.parse(tokens[i+1].strip())
            if right in ['<syntax-error>','<underfined>','<underflow>','<overflow>']:
                return right
            try:
                if op =='+':
                    left+=right
                elif op=='-':
                    left-=right
                elif op=='*':
                    left*=right
                elif op=='/':
                    left//=right
            except OverflowError:
                if left>0:
                    return '<overflow>'
                else:
                    return '<underflow>'
        return left

calc=Calculator()
out=[]
while True:
    try:
        line=input().strip()
        if not line:
            break
        result=calc.evalute(line)
        out.append(result)
    except EOFError:
        break

for _ in out:
    if _ :
        print(_)