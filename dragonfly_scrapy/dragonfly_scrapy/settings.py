# Scrapy settings for dragonfly_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import imp, os
import sys

BOT_NAME = 'dragonfly_scrapy'

SPIDER_MODULES = ['dragonfly_scrapy.spiders']
NEWSPIDER_MODULE = 'dragonfly_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/17.0 Firefox/17.0'
DOWNLOAD_DELAY = 0.7
#CURRENT_REQUESTS = 500
#LOG_LEVEL = 'INFO'

#ITEM_PIPELINES = [
#    'dragonfly_scrapy.pipelines.ProductPipeline',
#    ]

def setup_django_env(path):
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)

    # Add django project to sys.path
    sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))

django_project_path = os.path.realpath(os.path.join(os.path.dirname(__file__),'../../dragonfly/dragonfly'))
setup_django_env(django_project_path)
