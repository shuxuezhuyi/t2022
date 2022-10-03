#!/usr/bin/python3
# 用 preamble-for-plasTeX.tex 的内容替换掉 t2022.tex 的导言(preamble)部分

import os

here = os.path.dirname(os.path.realpath(__file__))
preamble_path = here + '/preamble-for-plasTeX.tex'
tex_path = here + '/t2022.tex'

with open(preamble_path, 'r', encoding='utf-8') as preamble_file:
    write_lines = preamble_file.readlines()
write_lines.append('\n') # 追加空行, 免得下边加的 \begin{document} 被加到行尾
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
        else: write_lines.append(line.replace(r'\checkmark ', '✓')) # 在这里查找替换也是拓展 plasTeX 功能的方法(大概)
    tex_file.writelines(write_lines)

