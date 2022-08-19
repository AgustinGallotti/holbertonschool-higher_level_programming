#!/usr/bin/python3
"""module"""


if __name__ == '__main__':
	import urllib.request


	url = 'https://intranet.hbtn.io/status'
	status_code = urllib.request.urlopen(url)
	with status_code as response:
		st = response.read()
		print(st)
