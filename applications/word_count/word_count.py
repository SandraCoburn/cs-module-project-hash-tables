import re
def word_count(s):
    d = {}
    #ignored = ['"', ':', ';', ',', '.', '-','+','=','\\','|','[',']','{', '}', '(', ')','*', '^', '&', '/']
  
  
    words = s.lower().split()
    for w in words:
        w = re.sub(r'[^\w\']+', '', w)
        if w == "":
            continue
        if w not in d:
            d[w] = 0
        d[w] += 1
        
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))