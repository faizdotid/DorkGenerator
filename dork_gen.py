#simple dork generator from file
def splitss(text: str) -> list:
    _textsplit = text.split(' ')
    __textsplit = list(dict.fromkeys(_textsplit))
    return __textsplit

def maker(file: str) -> None:
    text = open(file, mode='r', encoding='utf-8').read().replace('\n', '').replace('\r', '')
    _text = splitss(text)
    dork1 = input('first text ? ')
    dork2 = input('end text ? ')
    print('Generate {} dork'.format(len(_text)))
    for dork in _text:
        out = list()
        out.extend([dork1, dork, dork2])
        outp = ' '.join([dup for dup in out if dup != ''])
        with open('generated_dorks.txt', mode='a', encoding='utf-8') as exc:
            exc.write(outp + '\n')

def main():
    print('DORK MAKER !!!\n')
    file = input('file ? ')
    maker(file)

if __name__ == '__main__':
    main()
