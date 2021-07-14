# Proteins perform every practical function in the cell.
# Protein domain = a structural and functional unit of the protein.
# Each domain usually corresponds to a single function of the protein. Some proteins have only one domain,
# but many proteins are multifunctional and therefore possess several domains.
# Protein family = A homologous group of proteins. Usually have the same set of domains, performing similar functions.
# Motif = a component of a domain essential for its function; usually evolutionary conservative.
# UniProt = a central repository for protein data.

# Protein motif representation = [XY] = "either X or Y"; {X} = "any amino acid except X"
# Given: At most 15 UniProt Protein Database access IDs
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by
#         a list of locations in the protein string where the motif can be found.
# Tip: N-glycosylation motif is written as N{P}[ST]{P}

# 1. Read in the input file
# 2. Obtain the FASTA files for each access IDs
# 3. Check if the amino acid sequence for each protein contains pattern N{P}[ST]{P}
# 4. If there are pattern matches, add the locations (the position in a string where the substring begins)
# 5. Write to the output file the access IDs and the corresponding locations of N-glycosylation motifs for the protein sequence

import urllib.parse
import urllib.request

url = 'https://www.uniprot.org/uploadlists/'
s = 'B5ZC00 A2Z669 P07204_TRBM_HUMAN P20840_SAG1_YEAST'

params = {
'from': 'ACC+ID',
'to': 'ACC+ID',
'format': 'fasta',
'query': s
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
   response = f.read()
print(response.decode('utf-8'))
