s = input()

prev_s = s[:]
s = s[s.find('h') + 1:s.rfind('h')]
s = s.replace('h', 'H')
s = prev_s[:prev_s.find('h') + 1] + s + prev_s[prev_s.rfind('h'):]
print(s)
