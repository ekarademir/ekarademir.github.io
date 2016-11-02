import markdown
import codecs
import re
from os import listdir

def decorate(mdfile, templatefile = './template.thtml'):
    """Inserts the converted markdown text into a template html file."""

    # Load the template file
    tmpf = codecs.open(templatefile, 'r', 'utf-8')
    template = tmpf.read()

    # Load the markdown text
    mdf = codecs.open(mdfile, 'r', 'utf-8')
    mdtext = mdf.read()

    content = template.replace(u"{{CONTENT}}", markdown.markdown(mdtext), 1)

    # Second pass to correct .md links
    content = re.sub(r'href.*\.md', mdrepl, content)

    outfile = mdfile.replace('.md','.html')

    outf = codecs.open(outfile, "w",
                          encoding="utf-8",
                          errors="xmlcharrefreplace")
    outf.write(content)

    # Report
    print(outfile)

    tmpf.close()
    mdf.close()
    outf.close()


def convertall():
    """Convert all md files in the directory to html files. Ignore listed ones"""

    ignore = ['README.md', 'TODO.md']

    for mdfile in listdir('.'):
        if mdfile[-3:] == '.md' and mdfile not in ignore:
            decorate(mdfile)

def mdrepl(matchobj):
    s = matchobj.group(0)

    return s[:-2]+"html"

if __name__ == '__main__':
    convertall()
