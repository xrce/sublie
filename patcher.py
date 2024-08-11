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
    else: raise Exception("Pattern not found")

infile = input("Input file : ") if not args.infile else args.infile
outfile = infile if not args.outfile else args.outfile

try: replace_hex(infile, outfile, b"\x80\x78\x05\x00\x0F\x94\xC1", b"\xC6\x40\x05\x01\x48\x85\xC9")
except: replace_hex(infile, outfile, b"\x80\x79\x05\x00\x0F\x94\xC2", b"\xC6\x41\x05\x01\xB2\x00\x90")
