import sys
import os
import argparse

from string import Template

from pkg_resources import resource_string, resource_filename

PACKAGE = 'findbyanswers_website'


def main(server_name):
    nginx_template = resource_string(PACKAGE, 'configuration/nginx_template.conf')
    nginx_template_unicode = unicode(nginx_template)
    root = os.path.abspath(resource_filename(PACKAGE, 'static'))
    template = Template(nginx_template_unicode)
    print template.substitute(root=root, server_name=server_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate nginx configuration file')
    parser.add_argument('--server-name', default='localhost', help='server_name value')

    args = parser.parse_args()
    sys.exit(main(server_name=args.server_name))
