def fun(s):
    # return True if s is a valid email, else return False
    if s.count('.') == 1 and s.count('@') == 1:
        if len(s[s.index('.')+1:]) <=  3 and '_' not in s[s.index('@'):] and '/' not in s[s.index('@'):]:
            if s[:s.index('@')] != '' and '!' not in s[:s.index('@')] and '#' not in s[:s.index('@')] and '$' not in s[:s.index('@')] and '%' not in s[:s.index('@')] and '^' not in s[:s.index('@')] and '&' not in s[:s.index('@')] and '*' not in s[:s.index('@')] and '(' not in s[:s.index('@')]:
                return True
    else:
        return False
