#!/usr/bin/python3
''' test arg parsing '''

# %%
import argparse

# %%
infile = type = None

# %%


def main():
    global infile, type

    ap = argparse.ArgumentParser(
        description='test description')
    ap.add_argument('-t', '--type', required=True, help='type of parsing')
    ap.add_argument('-f', '--file',
                    help='file to parse')
    args = ap.parse_args()
    print('ap:', ap, '\nusage:', ap.usage)

    if (args.file is not None):
        print(f'args.file: {args.file} type: {type(args.file)}')
        infile = open(args.file)

    print('t=', args.type)
    type = args.type


# %%
'hello'


# %%
if __name__ == "__main__":
    main()
    quit()

# %%
