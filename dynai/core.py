import os
import random
import time

from bs4 import BeautifulSoup
import requests
import validators
from dynai.Handler import WrongURLProvided


class core:
    def __init__(self, url):
        """The constructor of the Scraper.

        :param url: Requests a url parameter for the core. The URL must be accessible through the internet. Expected pattern 'https://www.example.com'
        :type url: str
        """
        self._output_dir = None
        self._word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        self._response = requests.get(self._word_site)
        self._WORDS = self._response.content.splitlines()
        self.rinta = random.randint(0, len(self._WORDS) - 1)
        self._name = self._WORDS[self.rinta]
        self._name = str(self._name).replace("b'", "")
        self._name = str(self._name).replace("'", "")
        self._url = ""
        self._output_dir = "output"
        self._keepfiles = 3
        if validators.url(url):
            self._url = url
        else:
            raise WrongURLProvided(url, "")
        self._page = requests.get(self._url)
        self._bs = BeautifulSoup(self._page.content, 'html.parser').prettify()

    def set_name(self, name):
        """Sets the name of the core.
        :param name: This is the name of the core.
        :type name: str

        """
        self._name = name.lower().replace(" ", "")

    def get_name(self):
        """Returns the name of the core instance
        :return: name of the core
        :rtype: str"""
        return self._name

    def set_output_dir(self, out):
        """Sets the output directory of the core.
        To generate a directors please refer to

        :param out: This is the path to the output directory
        :type out: str
        """
        self._output_dir = out

    def get_output_dir(self):
        """Returns the path to the output directory
        :return: path to the output directory
        :rtype: str"""
        return self._output_dir

    def scrape(self):
        """Scrapes the webpage defined in the constructor and returns the whole page as String
        :return: Webpage as a variable
        :rtype: str
        """
        return self._bs

    def scrape_to_output(self, extension):
        """Scrapes the webpage and converts the webpage to a file in the output directory with the specified _extension.
        If the folder does not exist the folder will be created.
        :param extension: Defines the output file format. Most likely you want html as a file _extension. If you select another file _extension, the function will paste the html content in the file with your _extension. Usually you don't want this but it is possible.'
            :argument: .htm, .html, htm, html, .xml, xml
        :type extension: str
        """
        os.chdir("../")
        _extension = extension.lower().replace(" ", "")
        if _extension == ".htm":
            _extension = "htm"
        if _extension == ".html":
            _extension = "html"
        if _extension == ".xml":
            _extension = "xml"

        try:
            os.chdir(self._output_dir)
        except OSError as e:
            os.mkdir(self._output_dir)
            os.chdir(self._output_dir)

        _i = 0
        while os.path.exists(f"{self._name}_{_i}.{_extension}"):
            _i += 1
        _f = open(f"{self._name}_{_i}.{_extension}", "w")
        _f.write(self.scrape())
        _f.close()

    def cleanup(self, keepme=0):
        """Cleans the output directory and keeps the number of most recent files.
        :param keepme: Defines the number of most recent to be kept (default: 0)
        :type keepme: int
        """
        os.chdir("../")
        self._keepfiles = keepme
        if self._keepfiles < 0:
            raise ValueError("The amount of files to be kept must be greater than 0.")
        elif self._keepfiles > 0:
            os.chdir(self._output_dir)
            _most_recent_files = ""
            _most_recent_time = 0
            _files = []
            for entry in os.scandir(os.curdir):
                if entry.is_file():
                    # get the modification time of the file using entry.stat().st_mtime_ns
                    _mod_time = entry.stat().st_mtime_ns
                    _files.append(entry.name)
                    if _mod_time > _most_recent_time:
                        # update the most recent file and its modification time
                        _most_recent_files = entry.name
                        _most_recent_time = _mod_time
            if len(_files) > self._keepfiles:
                i = len(_files) - 1
                while self._keepfiles <= i:
                    print(_files[i], end='')
                    os.remove(_files[i])
                    i -= 1
