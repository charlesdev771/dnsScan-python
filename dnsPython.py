##====================================================================##
##                                                                    ##
## SOFTWARE: DnsScan python.                                          ##
## AUTHOR: Charles Dantas (ccod)                                 ##
## VERSION: 0.1                                                       ##
## CREATION DATE: 04/06/2022                                          ##
##                                                                    ##
##====================================================================##

#!/usr/bin/python

import dns.resolver #To use this library: pip install dnspython

class Dnspython:

	def main(self):

		self.dnsScan() #Call the scan method


	def dnsScan(self):

		try:

			fileIn = str(input("The way of wordlist: ")) #Complete way of wordlist.
			target = str(input("Target: ")) #target
			res = dns.resolver.Resolver() #call the dns
			file = open(fileIn, 'r') #Open the wordlist
			subD = file.read().splitlines() #Read the wordlist	

			for subDD in subD:

				sub_target = subDD + ' . ' + target
				result = res.resolve(sub_target, 'A')
				for ip in result:

					print(sub_target, ' - > ', ip)

		except Exception as error:
			
			print(error)

dnsScan = Dnspython()
dnsScan.main()
