from core.util import add_closing_tag

inputs = ['../topics/orig/topics2017.txt',
          '../topics/orig/topics2005.txt',
          '../topics/orig/topics2004.txt'
          ]

outputs = ['../topics/topics2017.txt',
           '../topics/topics2005.txt',
           '../topics/topics2004.txt'
           ]

if __name__ == '__main__':
    for i in range(0, len(inputs)):
        add_closing_tag(inputs[i], outputs[i])