import dynai

if __name__ == '__main__':
    tools = dynai.core(url="https://www.python.org/dev/peps/pep")
    a = tools.scrape_to_output()
    print(tools.get_name())