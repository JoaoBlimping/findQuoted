import sys

def main():
    text = sys.stdin.read()
    if (len(text) == 0):
        print("it fucked up because you added no text")
        return
    if (len(sys.argv) != 2):
        print("there was only meant to be one command line argument mate, it's the search string")
        return
    target = sys.argv[1]
    start = -1
    for i,c in enumerate(text):
        if (c == '\'' or c == '\"'):
            if (start == -1):
                start = i
            elif (text[start] == text[i]):
                sub = text[start + 1:i]
                if (target in sub): print(sub)
                start = -1

main()
