# Because the GC-content throughout the genome differs between species, GC-content can offer a rough preliminary test
# of the identity of unknown DNA. Coding regions of the genome have a tendency to contain a higher percentage of
# guanine and cytosine ("GC-rich region"). Thus, just as GC-content between species offer a rough test of species identity,
# testing the GC-content of a snippet of DNA from a known species can offer insight into whether that DNA may belong to a gene.

# Most prokaryotes have a GC-content significantly higher than 50% --> GC content can be used to differentiate prokaryotes ane eukaryotes

# Given: At most 10 DNA strings in FASTA format
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string

s = 'AGCTATAG'

def gc_content(dna):
    count = 0
    for n in dna:
        if n == 'C' or n == 'G':
            count += 1
    return count / len(dna) * 100

f = open("rosalind_gc.txt", "r")

lst = f.read().splitlines()

lines = {}
for line in lst:
    if line.startswith('>'):
        id = line[1:]
        lines[id] = ''
    elif lines[id] == '':
        lines[id] = line
    else:
        # print(line)
        lines[id] = lines[id] + line

gc_dict = dict((k, gc_content(v)) for k, v in lines.items())

max_gc = max(gc_dict, key=gc_dict.get)

print(lines)
print(gc_dict)
print(max_gc, gc_dict[max_gc])



