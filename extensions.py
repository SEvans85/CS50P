extension = input('What is the name of your file? ')
extension = extension.lower()

match extension:
    case extension.endswith('gif'):
        print('image/gif')
    case extension.endswith('jpg'):
        print('image/jpg')
    case extension.endswith('jpeg'):
        print('image/jpeg')
    case extension.endswith('png'):
        print('image/png')
    case extension.endswith('pdf'):
        print('adobe/pdf')
    case extension.endswith('txt'):
        print('text/txt')
    case extension.endswith('zip'):
        print('compression/zip')

if extension.endswith('gif'):
    print('image/gif')
elif extension.endswith('jpg')




