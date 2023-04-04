def rep_char (n) :
    print ('-' * n )

def draw_line_string(msg1, msg2) : 
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char(nstr)
    print(f'{msg1},\n{msg2} ')
    rep_char(nstr)


name = input('Input his/her name: ')

draw_line_string ('Hello '+ name , "welcome to seoul.")