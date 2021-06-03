# ptables
A Shameless Ripoff of Rainbow Tables, which stores precomputed hashes in a CSV File which can be later Greped out out Parsed out using Some tool! Currently, More Work Needed!

<h1>The CSV-Based module</h1>
This module supports the following Algorithms:<br>
<code>
<pre>
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
</pre>
</code>
<h3>Command Line Arguments</h3>
<pre>
<code>
usage: csv_maker.py [-h] [--wordlist WORDLIST] [--output OUTPUT]
                    [--algorithm ALGORITHM]

optional arguments:
  -h, --help            show this help message and exit
  --wordlist WORDLIST   Use this Wordlist </path/to/file> (Mandatory)
  --output OUTPUT       Use this Option to save the output (Default:
                        Terminal)
  --algorithm ALGORITHM
                        Use this Option to specify the Algorithm, or use --list_algorithms to list them
                        (Default: MD5)
</code>
</pre>

<h3>Using the Output</h3>
Since, all the Hashes are Saved as <code>kevin1,sha256,b96e47cc910f7e99b3fd78142da92034c9f6fa57bf9a21a7152cf8fe90cb87f4,-</code>, where First Column is Password, Second Algorithm, Third Hash and Fouth Salt<br>
Anyone can Use this in their Favour by Using Custom tools, Office Applications, or Even Grep in Bash shell!<br>
For Finding a Hash: <code>cat csv_file.csv |grep '6161b0a284159565a0f7d5df2dd2698b5f87906cd91ff5322caf179b451f5a41'</code><br>
For Finding a Password: <code>cat csv_file.csv |grep 'kevin1'</code><br>
For Finding Hashes/Passwords with Same Algorithm: <code>cat csv_file.csv |grep 'md5'</code><br>
