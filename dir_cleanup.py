import os, sys
import send2trash

# list for files to keep
WHITELIST = []

# extensions to delete
EXTENSIONS = [
    ".ics"
    ".exe",
    ".msi",
    ".tar",
    ".zip"
]

def main():
    try:
        # get specified directory
        path = sys.argv[1]
    except IndexError:
        print('Usage: dir_cleanup.py [path=\'.\']')

    # set default path
    path = '.'

    # iterate over files
    for filename in os.listdir(path):
        if filename in WHITELIST:
            continue
        elif os.path.splitext(filename)[1] in EXTENSIONS:
            send2trash.send2trash(filename)

# check if main thread
if __name__ == '__main__':
    main()