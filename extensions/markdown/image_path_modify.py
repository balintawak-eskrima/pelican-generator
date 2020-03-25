from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
import re


class ImagePathModifyTreeprocessor(Treeprocessor):
    def run(self, root):
        for img in root.getiterator('img'):
            img.set('src', re.sub(r'\.\.(/)', r'\1', img.get('src')))


class ImagePathModifyExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            ImagePathModifyTreeprocessor(md),
            'image_path_modify',
            15,
        )


def makeExtension(**kwargs):
    return ImagePathModifyExtension(**kwargs)
