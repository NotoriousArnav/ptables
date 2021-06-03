#!/usr/bin/env python3
#UTF-8
import csv
import hashlib
import sys
import argparse
import os

__AUTHOR__ = 'Arnav Ghosh'
__WEBSITE__ = 'https://arnavghosh0official2004.pythonanywhere.com'

supported_algorithm = {
	'md5':hashlib.md5,
	'sha256': hashlib.sha256,
	'sha3_224':hashlib.sha3_224,
	'sha384':hashlib.sha384,
	'sha224':hashlib.sha224,
	'sha512': hashlib.sha512,
	'sha3_256': hashlib.sha3_256,
	'blake2s':hashlib.blake2s,
	'sha1':hashlib.sha1,
	'shake_128':hashlib.shake_128,
	'sha3_384':hashlib.sha3_384,
	'blake2b':hashlib.blake2b,
	'shake_256':hashlib.shake_256,
	'sha3_512':hashlib.sha3_512
}

list_supported_algo = lambda: print(f'Supported Algorithms are \n{[x for x in supported_algorithm.keys()]}')

#System Argument for Listing Algos
if '--list_algorithms' in sys.argv:
	list_supported_algo()
	sys.exit()

#System Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--wordlist", help='Use this Wordlist </path/to/file> (Mandatory)')
parser.add_argument("--output", help='Use this Option to save the output (Default: Terminal)')
parser.add_argument("--algorithm", help='Use this Option to specify the Algorithm (Default: MD5)')
#parser.add_argument("--list_algorithms", help='Use this options to List Algorithms')
args = parser.parse_args()

def append_to_csv(data, file_path, verbose=False):
	file = open(file_path, 'a')
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(data)
	if verbose:
		print(f'Written {data}')
	file.close()

flags = dict()

#Verify the System Arguments
#Path to wordlist
if os.path.exists(args.wordlist):
	print(f"{args.wordlist} File Exists")
	flags['wl'] = args.wordlist
else:
	raise Exception(f"{args.wordlist} File Doesn't Exist")

#Path to Output file, or No Output file
if args.output:
	flags['out'] = {'type':'file', 'location':args.output}
	print(f"{args.output} : Output will be saved at this Location")
else:
	flags['out'] = {'type':'dump', 'location': 'terminal'}
	print("Output Will be dumped in the terminal")

#Algorithm
if args.algorithm:
	print(f"Will be Using {args.algorithm}")
	if args.algorithm in supported_algorithm:
		flags['algo'] = supported_algorithm[args.algorithm]
		flags['algo_name'] = args.algorithm
		print(f"{args.algorithm} is Supported, Will be Used!")
	else:
		flags['algo'] = hashlib.md5
		flags['algo_name'] = 'md5'
		print(f'Supported Algorith are {supported_algorithm}')
		raise Exception("Algorithm Not Supported")
else:
	flags['algo'] = hashlib.md5
	flags['algo_name'] = 'md5'
	print("MD5 will be Used")

print(flags)

#Read the File and Compute the results
with open(flags['wl']) as wordlist:
	for password in wordlist:
		n = n +1
		password = password.replace('\n', '')
		hash_ = flags['algo'](str(password).encode()).hexdigest()
		if flags['out']['type'] == 'file':
			append_to_csv([password, flags['algo_name'], hash_, '-'], flags['out']['location'])
		else:
			print(f"{password},{args.algorithm},{hash_},-")

print("Your CSV File is ready to go!")
print(f"A Program By {__AUTHOR__}, For any support visit {__WEBSITE__}")
