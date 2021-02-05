"""Squaring tool"""
import argparse

__version__ = '0.1'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', help='Number to square', type=int)
    ap.add_argument('--inv', help='Number to square', action='store_true')
    arguments = ap.parse_args()

    n = abs(arguments.n)

    ref = 0
    for i in range(n):
        ref += n
    if args.inv:
        print (1.0/ref)
    else:
        print(ref)

if __name__ == '__main__':
    main()
