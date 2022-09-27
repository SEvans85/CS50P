extension = input('What is the name of your file? ')

match extension:
    case extension.endswith('gif'):
        print('Your file is a .gif')
    case extension.endswith('jpg'):
        print('Your file is a .jpg')
    case extension.endswith('jpeg'):
        print('Your file is a .jpeg')
    case extension.endswith('png'):
        print('Your file is a .png')
    case extension.endswith('pdf'):
        print('Your file is a .pdf')
    case extension.endswith('txt'):
        print('Your file is a .txt')
    case extension.endswith('zip'):
        print('Your file is a .zip')





