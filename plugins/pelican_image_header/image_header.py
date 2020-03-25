from pelican import signals
from pelican.readers import MarkdownReader
import re
from markdown import Markdown
from pelican.utils import pelican_open


class MarkdownExtendedReader(MarkdownReader):

    enabled = bool(Markdown)
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']

    def __init__(self, *args, **kwargs):
        super(MarkdownExtendedReader, self).__init__(*args, **kwargs)

    def extract_header_image(self, content):
        class _Extractor(object):
            def __init__(self):
                self.image_header = None

            def __call__(self, found):
                self.image_header = found.group(2)

        _extractor = _Extractor()
        regex = r'(?<=^---$)\s*\!\[[^\]]*]\((\.*)?([^\)]+)\)'
        modified = re.sub(regex, _extractor, content, count=1, flags=re.MULTILINE)
        return modified, _extractor.image_header

    def read(self, source_path):
        """Parse content and metadata of markdown files"""
        image = None

        self._source_path = source_path
        self._md = Markdown(**self.settings['MARKDOWN'])
        with pelican_open(source_path) as text:
            text_modified, image = self.extract_header_image(text)
            content = self._md.convert(text_modified)

        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
            metadata['image'] = image
        else:
            metadata = {}
        return content, metadata


def add_reader(readers):
    readers.reader_classes['md'] = MarkdownExtendedReader
    readers.reader_classes['markdown'] = MarkdownExtendedReader
    readers.reader_classes['mkd'] = MarkdownExtendedReader
    readers.reader_classes['mdown'] = MarkdownExtendedReader


def register():
    signals.readers_init.connect(add_reader)
