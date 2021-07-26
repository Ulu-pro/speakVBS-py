try:
    import os
except ImportError:
    input('Установите библиотеку "os" для Python...')
    exit()

def speak(text, fname='demo'):
    f = open("%s.vbs" % fname, "w") # make, then open the file
    f.write("""Dim speaks, speech
    speaks="%s"
    Set speech=CreateObject("sapi.spvoice")
    speech.Speak speaks
    with speech
    .Volume = 100
    .Rate = 4
    end with""" % text) # overwrite the file
    f.close() # close
    os.system("start %s.vbs" % fname) # sound

print('=== Для выхода введите "exit()" === \n','-'*10)
while 1:
    text = input('Что мне сказать? ')
    if text == 'exit()':
        exit()
    speak(text)
    print('-'*10)
