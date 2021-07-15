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

import re
import urllib.parse
import urllib.request

url = 'https://www.uniprot.org/uploadlists/'
s = 'P00750_UROT_HUMAN P00740_FA9_HUMAN P17967 P07357_CO8A_HUMAN P01046_KNL1_BOVIN P10153_RNKD_HUMAN P01190_COLI_BOVIN Q82ZQ1 P55067_PGCN_RAT A1TJ10 P10643_CO7_HUMAN B9LIC8 P08198_CSG_HALHA P42098_ZP3_PIG Q50228'

params = {
'from': 'ACC+ID',
'to': 'ACC',
'format': 'fasta',
'query': s,
'include': 'no'
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
   response = f.read()
print(response.decode('utf-8'))
sequences = response.decode('utf-8').splitlines()
ids = s.split(' ')
print(ids)
print(len(ids))
count = 0
seq_dic = {}
# pattern = '\\|.*\\|'
# for i in sequences:
#     if i.startswith('>'):
#         id = re.findall(pattern, i)[0][1:-1]
#         print(id)

for p in sequences:
    if p.startswith('>'):
        seq_dic[count] = ''
        count += 1
        print(count)
    else:
        seq_dic[count - 1] += p

print(seq_dic)

n_gly_pat = '(?=(N[^P][ST][^P]))'

# loc_dic = {}
# for key, seq in seq_dic.items():
#     # print(key, ids[key])
#     # print(seq)
#     locations = [match.start() + 1 for match in re.finditer(n_gly_pat, seq_dic[key])]
#     if locations:
#         loc_dic[ids[key]] = locations
#     else:
#         continue

#print(loc_dic)

# output = open("Output_Finding_a_Protein_Motif.txt", 'w+')
# for id, locs in loc_dic.items():
#     output.write(id + "\n")
#     output.write(' '.join(str(loc) for loc in locs) + "\n")
# output.close()

