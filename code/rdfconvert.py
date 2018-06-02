import os, glob
import rdflib
# import rdflib-jsonld
from rdflib import Graph, plugin
from rdflib.serializer import Serializer


# read all the files from this directory
input_path = "../data/*/."
output_path = "../data/all_rdf.ttl"

filenames = []
contents = ''
for infile in glob.glob( os.path.join(input_path, '*.*') ):
     # print("current file is: " + infile)
    filenames.append(infile)

with open(output_path, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            contents = infile.read()
            g = Graph().parse(data=contents, format='json-ld')
            rdf = g.serialize(format='turtle')
            print(infile)

            for line in rdf:
                outfile.write(line)

print("done!")
