import re



welcomeContent = """

               Welcome to the 'MADLIB' Game                   
            Simply we will ask u some Quastions             
       Then you will have a fuuny story for these answers 
                    So lets have fun!!!                        
 """
print(welcomeContent)

path='assets/make_me_a_video_game_template.txt'

""" functon to read text  with input: path and return : the  text in file """

def read_template(path):
   with open(path) as file:
       data =file.read()
   return (data)

# inputs function to resives data 
def inputs(data):
 
    input_list =[]
    print("        So Enter These list AND don't mess it:   " )
    for x in range(21):
        input_list += [input(f'{data[x]} :')]
    return tuple ( input_list)

""" function find all word in {} and formated with new input by user """

def parse_template(text):

    data=re.findall(r"\{(.*?)\}",text) 
    text=re.sub( r"\{(.*?)\}", '{}', text)
    return [text, tuple(data)]

""" function to merge the new inputs with the text in file """

def merge(pars1,pars2):
   return( pars1.format( *pars2 ) )



def mad_save():
    content = read_template('assets/make_me_a_video_game_template.txt')
    text, ports = parse_template(content)
    inputs = []
    for i in ports:
        input_va = input(f"Entert a {i}:  ")
        inputs.append(input_va)
    story = merge(text, inputs)
    print(story)

    with open('assets/madlib_output.txt', 'w')as f:
        f.write(story)

if __name__ == '__main__':
    mad_save()