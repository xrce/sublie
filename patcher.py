import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-i', help='Input file', dest='infile')
parse.add_argument('-o', help="Output file", dest='outfile')
args = parse.parse_args()

def replace_hex(infile, outfile, orig, patched):
    with open(infile, 'rb') as f: data = bytearray(f.read())
    start = data.find(orig)
    if start != -1:
        end = start + len(orig)
        data[start:end] = patched
        with open(outfile, 'wb') as f: f.write(data)
        print("File Patched")
    else: print("Pattern not found")

original = b"\x80\x78\x05\x00\x0F\x94\xC1"
replaced = b"\xC6\x40\x05\x01\x48\x85\xC9"

infile = input("Input file : ") if not args.infile else args.infile
outfile = infile if not args.outfile else args.outfile

replace_hex(infile, outfile, original, replaced)
