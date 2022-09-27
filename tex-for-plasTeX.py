#!/usr/bin/python3
import os

here = os.path.dirname(os.path.realpath(__file__))
preamble_path = here + '/preamble-for-plasTeX.tex'
tex_path = here + '/t2022.tex'

with open(preamble_path, 'r', encoding='utf-8') as preamble_file:
    write_lines = preamble_file.readlines()
with open(tex_path, 'r', encoding='utf-8') as tex_file:
    lines = tex_file.readlines()
with open(tex_path, 'w', encoding='utf-8') as tex_file:
    write_sign = False
    for line in lines:
        if not write_sign:
            if r'\begin{document}' in line: 
                write_sign = True
                write_lines.append(line)
            continue
        write_lines.append(line)
    tex_file.writelines(write_lines)

