from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor, NormalizeWhitespace
import logging
import yaml
import re

log = logging.getLogger('MARKDOWN')


class MetaYamlPreprocessor(Preprocessor):
    def run(self, lines):
        meta = {}
        content = '\n'.join(lines)

        parts = content.split('---', 2)
        if len(parts) > 2:
            metadata = yaml.safe_load(parts[1])

            for (k, v) in metadata.items():
                if type(v) is list:
                    meta[k] = [', '.join(v)]
                else:
                    meta[k] = [v]

            self.md.Meta = meta
            return re.split(r'\n', parts[2])

        return lines


class MetaYamlExtension(Extension):
    def extendMarkdown(self, md):
        """ Add MetaPreprocessor to Markdown instance."""
        md.registerExtension(self)
        self.md = md
        md.preprocessors.register(MetaYamlPreprocessor(md), 'meta', 27)

    def reset(self):
        self.md.Meta = {}


def makeExtension(**kwargs):
    return MetaYamlExtension(**kwargs)
