import re
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.


with open("applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()

ignored = ['"', "'",':', "?",'!','_',';', ',', '.', '-','+','=','\\','|','[',']','{', '}', '(', ')','*', '^', '&', '/']
ignored.append("''")

for char in ignored:
     words = words.replace(char, "")

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decoded_d = {}
for k, v in encode_table.items():
    decoded_d[v] = k
#print(decoded_d)
def crack_caesar(text):
    cache = {}
    #print(text.split())
    text = text.upper().split()
    for word in text:
        word = re.sub(r'[^\w\']+', '', word)
        if word.isspace():
            continue
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    
    return cache
#print(crack_caesar(words))

def decoded(s):
    r = ""
    for char in s:
        if char not in decoded_d:
            r += decoded_d[char]
    print(r)
    return r

# print(crack_caesar(words))
print(decoded(words))

