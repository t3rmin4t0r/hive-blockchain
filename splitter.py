import sys
import gzip 


def main(args):
	f = gzip.open(args[0], 'rb')
	out = None
	n = 0
	table = None
	for l in f:
		if (l.startswith("COPY")):
			table = l.split(" ")[1]
			out = open(table+".tsv", "w")
			n = 0
			print "Opening %s.tsv" % (table)
		elif (l.startswith("\\.")):
			print "Wrote %d rows into %s" % (n, table)
			out.close()
			out = None
		elif (out):
			n += 1
			out.write(l)
		else:
			print "SKIP: %s" % l


if __name__ == "__main__":
	main(sys.argv[1:])

# vim: ts=4 noet sw=4 ai
