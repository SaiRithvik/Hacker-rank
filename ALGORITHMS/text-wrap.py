import textwrap as tw

def wrap(string, max_width):

	return(tw.fill(string,max_width))


    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)