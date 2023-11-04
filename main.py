import dynai
import json

tools = dynai.core("https://www.python.org/dev/peps/pep")
tools.scrape_to_output("html")
print(tools.get_output_dir())
print(tools.get_name())
print(tools.scrape())

if __name__ == '__main__':
    words = open("words.txt", "rb")
    word_list = words.readlines()
    json_words = {word.rstrip(): "1" for word in word_list}
    words.close()
    js = open("json.json", )
    json.dumps(json_words, indent=4)
