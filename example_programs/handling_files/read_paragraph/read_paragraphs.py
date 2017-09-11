#
# Parse a file organized into paragraphs
#

n_interfaces = 0

def parse_interface(data):
    print("parsing interface with %i lines" % len(data))


with open('sla.txt') as f:
    paragraph = []
    for line in f:
        if line.startswith('!'):
            # save finished paragraph
            if paragraph and paragraph[0].startswith('interface'):
                parse_interface(paragraph)
                n_interfaces += 1
            paragraph = []
        else:
            paragraph.append(line)

    # remember to parse last paragraph
    if paragraph and paragraph[0].startswith('interface'):
        parse_interface(paragraph)
    

print("%i interfaces total" % (n_interfaces))

