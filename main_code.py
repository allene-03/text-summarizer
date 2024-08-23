def Modifier(boolean):
    import sys
    import re
    import string

    try:
        args = sys.argv[1:]
        #Ω≈ç√˜µµl˚åß©ßß∆˚¬œ∑´®†¥¨ˆø - symbols to choose from
        with open(args[1], 'r') as f:
            content = f.read()
            name = f.name
            print("\n\nOriginal File Contents: \n" + content + "\n--//(End)")

            delim = list(i for i in string.punctuation if i!="'")
            delim = delim + list('\n')
            punctuations = []
            for char in content:
                for punctuation in delim:
                    if punctuation == char:
                        punctuations.append(char)
                        content = content.replace(char, 'Ω')

            regexPattern = '|'.join(map(re.escape, delim))
            sentences = re.split(regexPattern, content)
            sentences = list(filter(None, sentences))

            l = []
            for sen in sentences:
                l.append(sen.split())
            sentences = l
            sentences = list(filter(None, sentences))

            with open('source/adjs.txt', 'r') as a:
                content_adj = a.read()
                words_adj = content_adj.split('\n')
                print("\n\nList Form of Sentences: \n" + str(sentences) + "\n")

                all_sentences = []
                for stri in sentences:
                    string = [i.lower() for i in stri]
                    words_adjec = [i.lower() for i in words_adj]
                    x = 0
                    new_sentence = []
                    for x in range(len(stri)):
                        if string[x] not in words_adjec:
                            new_sentence.append(stri[x])
                        x+=1
                    all_sentences.append(new_sentence)

                print("\n\nModified List Form of Sentences: \n" + str(all_sentences) + "\n")

                for thing in all_sentences:
                    all_sentences = ' '.join(thing)
                    break

                i = 0
                for character in all_sentences:
                    if character == 'Ω':
                        all_sentences = all_sentences.replace(character, punctuations[i], 1)
                        i+=1

                if boolean == True:
                    name_list = name.split('.')
                    name = name_list[0] + "_modified." + name_list[1]
                    with open(name, 'w') as n:
                        n.write(all_sentences)
                    print('\n\n||Output:\nWritten to file: {file}'.format(file=name))
                elif boolean == False:
                    print("\n\n||Output: \n" + all_sentences)
                else:
                    print("A fatal error has occured. Please report to project Github.")
    except (FileNotFoundError, IndexError):
        print('Please reference an accurate file in this directory (textSummarizer).\n')

def ArgumentErrors():
    print('''
Incorrect Usage:
    main.py -f <filename_with_extension>: [Summarizes given text file]
    main.py -fw <filename_with_extension>: [Summarizes given text file to external file]
    main.py --v: [Version of program]
    ''')

def Version():
    print('''
The current version for this Text Summarizer is {
    Version -- 1.09
}
To find out more information regarding version history, visit the project Github.
        ''')
