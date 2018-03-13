import sys, pyperclip,logging

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')



textOrigi = pyperclip.paste()
listOrigi = textOrigi.split()
logging.debug('origin text: \n')
logging.debug(listOrigi)
if '.' in listOrigi or '(' not in listOrigi or ');' not in listOrigi:
    logging.debug('text format error')
    print('text format error!!\n')
    print('the text may has been convertd before or it is not a verilog module port name text.\n')
    input('press "Enter" key to exit')
else:
    logging.debug(''.join(textOrigi))
    length_list = len(listOrigi)
    left = listOrigi.index('(')
    right = listOrigi.index(');')
    logging.debug(length_list)
    logging.debug(left)
    logging.debug(right)

    list_new = []
    #model name
    temp_name = listOrigi[0]
    add_name = temp_name + ' ' + temp_name
    list_new.append(add_name)
    #'('
    temp_name = listOrigi[1]
    list_new.append(temp_name)

    for temp_name in listOrigi[left+1:right-1]:
        #logging.debug(temp_name)
        length_port = len(temp_name)
        add_name = '\n\t.' + temp_name[0:length_port-1] + '(' + temp_name[0:length_port-1] + ')' + ','
        list_new.append(add_name)

    #last_port
    temp_name = listOrigi[right - 1]
    add_name = '\n\t.' + temp_name + '(' + temp_name + ')'
    list_new.append(add_name)
    #);
    add_name = '\n\t' + listOrigi[length_list-1]
    list_new.append(add_name)

    textNew = ''.join(list_new)
    pyperclip.copy(textNew)

    print('The orign module port text:\n')
    print(textOrigi)
    print('The new module port text:\n')
    print(textNew)
    
