class Cipher(object):
    """ Classe base para as cifras classicas """
    def format_str(self, text):
        '''
        Retorna text sem espacos e em maiusculas
        '''
        return text.replace(' ', '').upper()
 
    def shift_alphabet(self, alphabet, shift):
        '''
        Retorna alphabet com deslocamento de valor shift
        '''
        return alphabet[shift:] + alphabet[:shift]