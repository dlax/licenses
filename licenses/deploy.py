import sys
import os
from simplejson import dumps

class Deploy2Command(object):
    usage = """Create a series of flat files from the licenses database that
    can directly served by a web server.

Usage:
    %s <path> <hostname>"""

    service_version = '2.0'
    group_names = ['all_alphabetical', 'ckan_original', 'ckan_canada', 'ukgov']

    def run(self):
        if len(sys.argv) != 3:
            print "Usage: %s" % self.usage
            sys.exit(1)
        self.path = os.path.join(sys.argv[1], self.service_version)
        self.server_name = sys.argv[2]
        if os.path.exists(self.path):
            print "Error: Path already exists: %s" % self.path
            sys.exit(2)
        print ""
        print "Creating licenses service v%s in: %s" % (self.service_version, os.path.abspath(self.path))
        os.makedirs(self.path) # Will except if there isn't permission.
        self.path = os.path.abspath(self.path)
        self.write_group_files()
        self.write_apache_config()
        self.write_apache_vhost()
        self.print_further_instructions()

    def write_group_files(self):
        print ""
        print "Writing JSON licenses group files..."
        from licenses import Licenses
        licenses = Licenses()
        for group_name in self.group_names:
            group_licenses = licenses.get_group_licenses(group_name)
            group_json = dumps(group_licenses, indent=2)
            file_path = os.path.join(self.path, group_name)
            file = open(file_path, 'w')
            file.write(group_json)
            file.close()
            print "'%s' has %s licenses: %s" % (group_name, len(group_licenses), file_path)
           
    def write_apache_config(self):
        config_content = ""
        for group_name in self.group_names:
            url_path = "/%s/%s" % (self.service_version, group_name)
            group_file_path = os.path.join(self.path, group_name)
            config_content += "Alias %s %s\n" % (url_path, group_file_path)
        config_file_path = self.get_apache_config_file_path()
        print ""
        print "Writing Apache config file: %s" % config_file_path
        config_file = open(config_file_path, 'w')
        config_file.write(config_content)
        config_file.close()

    def get_apache_config_file_path(self):
        return os.path.join(self.path, 'licenses-httpd.conf')

    def get_apache_vhost_file_path(self):
        return os.path.join(self.path, '%s-vhost.conf' % self.server_name)

    def write_apache_vhost(self):
        vhost_file_path = self.get_apache_vhost_file_path()
        print "Writing example Apache VirtualHost file: %s" % vhost_file_path
        vhost_template = """
<VirtualHost *:80>
    ServerName %s
    Include %s
</VirtualHost>
        """
        config_file_path = self.get_apache_config_file_path()
        vhost_config = vhost_template % (self.server_name, config_file_path) 
        vhost_file = open(vhost_file_path, 'w')
        vhost_file.write(vhost_config)
        vhost_file.close()

    def print_further_instructions(self):
        print ""
        print "Finish by enabling the example Apache virtual host (or make your own)."
        print ""
        print "Then restart Apache and check the service is working:"
        for group_name in self.group_names:
            print "  http://%s/%s/%s" % (self.server_name, self.service_version, group_name)
        print ""


if __name__ == "__main__":
    Deploy2Command().run()
