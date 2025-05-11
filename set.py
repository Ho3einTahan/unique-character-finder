def uniqueCharacterFinder(text):
    uniqueChar=set()
    for ch in text:
        if(ch in uniqueChar):
            uniqueChar.remove(ch)
        else :
            uniqueChar.add(ch)
            
    print(uniqueChar)
    
uniqueCharacterFinder("alii")