if s.startswith(")") or s.startswith(']') or s.startswith('}'):
    return False

stack = []
complement = {'(': ')', '{': '}', "[": "]"}

for i in s:
    if s.startswith(")") or s.startswith(']') or s.startswith('}'):
        return False

    elif i == '[' or i == '{' or i == '(':
        stack.append(i)

    elif len(stack) >= 1 and i == complement[stack[-1]]:
        stack.pop()

    else:
        return False

return True if len(stack) == 0 else False
