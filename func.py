def find_opposite_bracket(input_str):
        if input_str == '{':
            return '}'
        elif input_str == '[':
            return ']'
        elif input_str == '(':
            return ')'
        elif input_str == '}':
            return '{'
        elif input_str == ']':
            return '['
        elif input_str == ')':
            return '(' 
        else:
            return False