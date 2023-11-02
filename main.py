import dynai

if __name__ == '__main__':
    tools = dynai.core("https://www.python.org/dev/peps/pep")
    tools.scrape_to_output("html")
    print(tools.get_output_dir())
    print(tools.get_name())