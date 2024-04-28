# assert number
num_esperado = 1
num_obtido = 2
#           condição do assert(> or < or ==)           Mensagem do erro do assert
assert num_esperado == num_obtido, f'Esperado {num_esperado}, Atual {num_obtido}'

# assert text

text_esperado = 'Selenium Webdriver'
text_obtido = 'Selenium webdriver'

assert text_esperado.lower() == text_obtido.lower(), f'Esperado {text_esperado}, Atual {text_obtido}'

# assert text in string
text_esperado = 'Selenium'
text_obtido = 'Selenium webdriver'

assert text_esperado in text_obtido, f'Esperado {text_esperado}, Atual {text_obtido}'

# assert is_displayed/is_enable/is_selected

'''
Interação com elementos, ver se o elemento esta desbalitado ou habilitado
ou selecionado.
'''