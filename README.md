# DynamicAI

**dynai** is a Python library that allows you to scrape web pages, cleanse data and save the content to a file. Currently it provides a simple interface for web scraping and file management. You can use DynAI to fetch the HTML content of a webpage, save it to a file, and clean up the output directory by keeping only the most recent files. In the future more features will be added

## Installation

You can install dynai using `pip`:

```
pip install dynai
```

## Usage

### Importing the Library

```python
from dynai import core
```

### Initialising the Scraper

```python
url = "https://www.example.com"
scraper = core(url)
```

### Scraping the Webpage

You can scrape the webpage and get the HTML content as a string:

```python
webpage_content = scraper.scrape()
```

### Saving the Webpage to a File

You can save the scraped webpage to a file in the output directory with a specified file extension (e.g., `.html`):

```python
extension = ".html"
scraper.scrape_to_output(extension)
```

### Setting Custom Name and Output Directory

You can set a custom name for the scraped content and specify the output directory:

```python
scraper.set_name("custom_name")
scraper.set_output_dir("custom_output_directory")
```

### Cleaning up the Output Directory

You can clean up the output directory and keep a specified number of most recent files:

```python
keep_files = 3
scraper.cleanup(keep_files)
```

## Documentation

### `class core(url)`

#### Methods

- `set_name(name)`: Sets the name of the core instance.
- `get_name() -> str`: Returns the name of the core instance.
- `set_output_dir(out)`: Sets the output directory of the core.
- `get_output_dir() -> str`: Returns the path to the output directory.
- `scrape() -> str`: Scrapes the webpage defined in the constructor and returns the whole page as a string.
- `scrape_to_output(extension)`: Scrapes the webpage and saves it to a file in the output directory with the specified extension.
- `cleanup(keepme=0)`: Cleans the output directory and keeps the specified number of most recent files.

## Example

```python
from dynai import core

url = "https://www.example.com"
scraper = core(url)
webpage_content = scraper.scrape()
scraper.set_output_dir("output")
scraper.scrape_to_output(".html")
scraper.cleanup(3)
```

This example scrapes the webpage, saves it to an HTML file in the "output" directory, and keeps the 3 most recent files in the output directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): For HTML parsing.
- [Requests](https://docs.python-requests.org/en/master/): For making HTTP requests.
- [Validators](https://validators.readthedocs.io/en/latest/): For URL validation.