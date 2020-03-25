from pelican import signals
import xml.etree.ElementTree as ET
import functools
import datetime
import pytz
from io import BytesIO
import os
import gzip


class SitemapContainer(object):
    def __init__(self):
        self.urlset = ET.Element('urlset', {'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'})

    def add_url(self, loc, lastmod, changefreq='weekly', priority=0.5):
        url = ET.SubElement(self.urlset, 'url')

        loc_et = ET.SubElement(url, 'loc')
        loc_et.text = loc

        lastmod_et = ET.SubElement(url, 'lastmod')
        lastmod_et.text = lastmod

        changefreq_et = ET.SubElement(url, 'changefreq')
        changefreq_et.text = changefreq

        priority_et = ET.SubElement(url, 'priority')
        priority_et.text = str(priority)

    def get_tree(self):
        return ET.ElementTree(self.urlset)

    def write(self, f, encoding='utf-8', xml_declaration=True):
        self.get_tree().write(f, encoding, xml_declaration)


def dt_unix_start(tzname):
    strtime = '1970-01-01'
    tz_local = pytz.timezone(tzname)
    dt_unix = tz_local.localize(datetime.datetime.strptime(strtime, '%Y-%m-%d'))
    return dt_unix


class SitemapGenerator(object):
    def __init__(self, context, settings, path, theme, output_path):
        self.context = context
        self.settings = settings
        self.path = path
        self.theme = theme
        self.output_path = output_path

    def generate_output(self, writer):
        articles = self.context['articles']
        pages = self.context['pages']
        siteurl = self.settings['SITEURL'] + '/'

        # extract home page
        home_page = next(filter(lambda i: i.save_as == 'index.html' and i.date, pages), None)
        if not home_page:
            raise Exception('index page is not defined or date not set')

        pages = list(filter(lambda i: i.save_as != 'index.html', pages))

        index_date = functools.reduce(
            lambda acc, item: max([acc, item.__dict__.get('modified', item.__dict__.get('date'))]),
            [home_page] + articles, dt_unix_start(self.settings['TIMEZONE']))

        sitemap_container = SitemapContainer()

        # add index page
        sitemap_container.add_url(
            siteurl,
            index_date.isoformat(),
            'daily',
            1.0
        )

        # add articles
        for item in articles:
            sitemap_container.add_url(
                siteurl + item.url,
                item.__dict__.get('modified', item.__dict__.get('date')).isoformat(),
                'weekly',
                0.8
            )

        # add static pages
        for item in pages:
            sitemap_container.add_url(
                siteurl + item.url,
                item.__dict__.get('modified', item.__dict__.get('date')).isoformat(),
                'weekly',
                1.0
            )

        sitemap_path = os.path.join(writer.output_path, 'sitemap.xml.gz')
        with gzip.open(sitemap_path, 'wb') as f:
            sitemap_container.write(f)


def get_generator(pelican):
    return SitemapGenerator


def register():
    signals.get_generators.connect(get_generator)
