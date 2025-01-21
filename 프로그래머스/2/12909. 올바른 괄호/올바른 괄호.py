def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(': # 스택에 아이템이 있으면서 마지막이 '('일 때
                stack.pop()
            else:
                return False
            
    return len(stack) == 0