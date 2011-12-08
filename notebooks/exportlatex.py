# <nbformat>2</nbformat>

# <codecell>

import sys, os
from IPython.nbformat import current
from IPython.utils.text import wrap_paragraphs

# <codecell>

def export_latex(fname):
    with open(fname) as f:
        nb = current.read(f, 'json')
    lines = ''
    for cell in nb.worksheets[0].cells:
        if cell.cell_type == u'code':
            lines += '\\begin{verbatim}\n'
            lines += '%s\n' % cell.input
            lines += '\\end{verbatim}\n'
            for output in cell.outputs:
                if output.output_type == u'pyout':
                    if hasattr(output, 'latex'):
                        lines += '%s\n' % output.latex
                    else:
                        lines += '\n'
                        lines += '\\begin{verbatim}\n'
                        lines += '%s\n' % output.text
                        lines += '\\end{verbatim}\n'
            lines += '\n'
        if cell.cell_type == u'markdown':
            paragraphs = wrap_paragraphs(cell.source)
            for p in paragraphs:
                lines += p
                lines += '\n\n'
    newfname = os.path.splitext(fname)[0] + '.tex'
    with open(newfname,'w') as f:
        f.write(lines.encode('utf8'))

# <codecell>

if __name__ == '__main__':
    fname = sys.argv[1]
    export_latex(fname)

