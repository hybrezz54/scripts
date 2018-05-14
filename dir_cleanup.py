import os, sys
import send2trash

# list for files to keep
WHITELIST = [
    "2016W2.pdf"
]

# extensions to delete
EXTENSIONS = [
    ".ics",
    ".exe",
    ".msi",
    ".tar",
    ".zip"
]

def main():
    # get specified directory
    try:
        path = sys.argv[1]
    except IndexError:
        path = '.'

    # inform user
    print(f'Deleting files at {os.path.abspath(path)}...')

    # iterate over files
    for filename in os.listdir(path):
        if filename in WHITELIST:
            continue
        elif os.path.splitext(filename)[1] in EXTENSIONS:
            print('Deleting ' + filename)
            send2trash.send2trash(filename)

# check if main thread
if __name__ == '__main__':
    main()