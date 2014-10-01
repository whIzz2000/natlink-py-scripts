# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.1I+, Wed Oct 01 16:47:50 2014

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <key> = ('alpha' | 'bravo' | 'charlie' | 'delta' | 'echo' | 'foxtrot' | 'golf' | 'hotel' | 'india' | 'juliett' | 'kilo' | 'lima' | 'mike' | 'november' | 'oscar' | 'papa' | 'quebec' | 'romeo' | 'sierra' | 'tango' | 'uniform' | 'victor' | 'whiskey' | 'xray' | 'yankee' | 'zulu' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '!' | '@' | '#' | '$' | '%' | '^' | '&' | '*' | '(' | ')' | '`' | '~' | '-' | '_' | '=' | '+' | '\\' | '|' | '[' | '{' | ']' | '}' | ';' | ':' | "'" | '"' | ',' | '<' | '.' | '>' | '/' | '?' | 'Left' | 'Right' | 'Up' | 'Down' | 'space-bar' | 'tab-key' | 'Enter' | 'page-up' | 'page-down' | 'Backspace' | 'delete' | 'Escape' | 'Home' | 'End' ) ;
        <1> = 'Press' <key> ;
        <2> = <key> 'Here' ;
        <3> = 'Space Bar' ;
        <4> = 'Tab Key' ;
        <special> = ('Left' | 'Right' | 'Up' | 'Down' | 'space-bar' | 'tab-key' | 'Enter' | 'page-up' | 'page-down' | 'Backspace' | 'delete' | 'escape' ) ;
        <mod> = 'Shift' | 'control-key' | 'Alt' ;
        <nn> = ('one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine' | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50) ;
        <5> = 'Press' <special> <nn> ;
        <28> = (('Left' | 'Right' | 'Up' | 'Down' | 'space-bar' | 'tab-key' | 'Enter' | 'page-up' | 'page-down' | 'Backspace' | 'delete' | 'escape' ) ) <nn> ;
        <6> = 'Press' <mod> <key> <nn> ;
        <29> = ('Shift' | 'control-key' | 'Alt' ) <key> <nn> ;
        <7> = 'Press' <mod> <mod> <key> <nn> ;
        <30> = ('Shift' | 'control-key' | 'Alt' ) <mod> <key> <nn> ;
        <8> = 'Press' <mod> <mod> <mod> <key> <nn> ;
        <31> = ('Shift' | 'control-key' | 'Alt' ) <mod> <mod> <key> <nn> ;
        <n> = ('zero' | 'one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine') ;
        <9> = 'zoom' ('in' | 'out' ) <n> ;
        <32> = 'zoom' ('in' | 'out' ) ;
        <10> = 'save' ;
        <11> = 'new tab' ;
        <12> = 'last' ;
        <13> = 'new window' ;
        <14> = 'next' <n> ;
        <15> = 'previous' <n> ;
        <16> = 'switch tab' <n> ;
        <17> = 'private' ;
        <18> = 'close' ;
        <19> = 'bookmark' ;
        <20> = 'tools' ;
        <21> = 'reload' ;
        <22> = 'back page' ;
        <23> = ('Copy' | 'Paste' | 'Go' ) ('Address' | 'URL' ) ;
        <24> = 'text box' ;
        <25> = 'show links' ;
        <26> = 'copy links' ;
        <27> = 'clear cash' ;
        <any> = <1>|<2>|<3>|<4>|<5>|<28>|<6>|<29>|<7>|<30>|<8>|<31>|<9>|<32>|<10>|<11>|<12>|<13>|<14>|<15>|<16>|<17>|<18>|<19>|<20>|<21>|<22>|<23>|<24>|<25>|<26>|<27>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'chrome','')
        if not window: return None
        self.firstWord = 0
        # Return if same window and title as before
        if moduleInfo == self.currentModule: return None
        self.currentModule = moduleInfo

        self.deactivateAll()
        title = string.lower(moduleInfo[1])
        if string.find(title,'') >= 0:
            for rule in self.ruleSet1:
                try:
                    self.activate(rule,window)
                except natlink.BadWindow:
                    pass

    def convert_number_word(self, word):
        if   word == 'zero':
            return '0'
        elif word == 'one':
            return '1'
        elif word == 'two':
            return '2'
        elif word == 'three':
            return '3'
        elif word == 'four':
            return '4'
        elif word == 'five':
            return '5'
        elif word == 'six':
            return '6'
        elif word == 'seven':
            return '7'
        elif word == 'eight':
            return '8'
        elif word == 'nine':
            return '9'
        else:
            return word

    def get_key(self, list_buffer, functional, word):
        if word == 'alpha':
            list_buffer += 'a'
        elif word == 'bravo':
            list_buffer += 'b'
        elif word == 'charlie':
            list_buffer += 'c'
        elif word == 'delta':
            list_buffer += 'd'
        elif word == 'echo':
            list_buffer += 'e'
        elif word == 'foxtrot':
            list_buffer += 'f'
        elif word == 'golf':
            list_buffer += 'g'
        elif word == 'hotel':
            list_buffer += 'h'
        elif word == 'india':
            list_buffer += 'i'
        elif word == 'juliett':
            list_buffer += 'j'
        elif word == 'kilo':
            list_buffer += 'k'
        elif word == 'lima':
            list_buffer += 'l'
        elif word == 'mike':
            list_buffer += 'm'
        elif word == 'november':
            list_buffer += 'n'
        elif word == 'oscar':
            list_buffer += 'o'
        elif word == 'papa':
            list_buffer += 'p'
        elif word == 'quebec':
            list_buffer += 'q'
        elif word == 'romeo':
            list_buffer += 'r'
        elif word == 'sierra':
            list_buffer += 's'
        elif word == 'tango':
            list_buffer += 't'
        elif word == 'uniform':
            list_buffer += 'u'
        elif word == 'victor':
            list_buffer += 'v'
        elif word == 'whiskey':
            list_buffer += 'w'
        elif word == 'xray':
            list_buffer += 'x'
        elif word == 'yankee':
            list_buffer += 'y'
        elif word == 'zulu':
            list_buffer += 'z'
        elif word == '0':
            list_buffer += '0'
        elif word == '1':
            list_buffer += '1'
        elif word == '2':
            list_buffer += '2'
        elif word == '3':
            list_buffer += '3'
        elif word == '4':
            list_buffer += '4'
        elif word == '5':
            list_buffer += '5'
        elif word == '6':
            list_buffer += '6'
        elif word == '7':
            list_buffer += '7'
        elif word == '8':
            list_buffer += '8'
        elif word == '9':
            list_buffer += '9'
        elif word == '!':
            list_buffer += '!'
        elif word == '@':
            list_buffer += '@'
        elif word == '#':
            list_buffer += '#'
        elif word == '$':
            list_buffer += '$'
        elif word == '%':
            list_buffer += '%'
        elif word == '^':
            list_buffer += '^'
        elif word == '&':
            list_buffer += '&'
        elif word == '*':
            list_buffer += '*'
        elif word == '(':
            list_buffer += '('
        elif word == ')':
            list_buffer += ')'
        elif word == '`':
            list_buffer += '`'
        elif word == '~':
            list_buffer += '~'
        elif word == '-':
            list_buffer += '-'
        elif word == '_':
            list_buffer += '_'
        elif word == '=':
            list_buffer += '='
        elif word == '+':
            list_buffer += '+'
        elif word == '\\':
            list_buffer += '\\'
        elif word == '|':
            list_buffer += '|'
        elif word == '[':
            list_buffer += '['
        elif word == '{':
            list_buffer += '{'
        elif word == ']':
            list_buffer += ']'
        elif word == '}':
            list_buffer += '}'
        elif word == ';':
            list_buffer += ';'
        elif word == ':':
            list_buffer += ':'
        elif word == '\'':
            list_buffer += '\''
        elif word == '"':
            list_buffer += '"'
        elif word == ',':
            list_buffer += ','
        elif word == '<':
            list_buffer += '<'
        elif word == '.':
            list_buffer += '.'
        elif word == '>':
            list_buffer += '>'
        elif word == '/':
            list_buffer += '/'
        elif word == '?':
            list_buffer += '?'
        elif word == 'Left':
            list_buffer += 'Left'
        elif word == 'Right':
            list_buffer += 'Right'
        elif word == 'Up':
            list_buffer += 'Up'
        elif word == 'Down':
            list_buffer += 'Down'
        elif word == 'space-bar':
            list_buffer += ' '
        elif word == 'tab-key':
            list_buffer += 'Tab'
        elif word == 'Enter':
            list_buffer += 'Enter'
        elif word == 'page-up':
            list_buffer += 'PgUp'
        elif word == 'page-down':
            list_buffer += 'PgDn'
        elif word == 'Backspace':
            list_buffer += 'Backspace'
        elif word == 'delete':
            list_buffer += 'Del'
        elif word == 'Escape':
            list_buffer += 'Esc'
        elif word == 'Home':
            list_buffer += 'Home'
        elif word == 'End':
            list_buffer += 'End'
        return list_buffer

    # 'Press' <key>
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('keys.vch', 20, '\'Press\' <key>', e)
            self.firstWord = -1

    # <key> 'Here'
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            call_Dragon('ButtonClick', 'ii', [])
            top_buffer += '{'
            word = fullResults[0 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('keys.vch', 21, '<key> \'Here\'', e)
            self.firstWord = -1

    # 'Space Bar'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += ' '
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('keys.vch', 23, '\'Space Bar\'', e)
            self.firstWord = -1

    # 'Tab Key'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_4(words[1:], fullResults)
        except Exception, e:
            handle_error('keys.vch', 24, '\'Tab Key\'', e)
            self.firstWord = -1

    def get_special(self, list_buffer, functional, word):
        if word == 'Left':
            list_buffer += 'Left'
        elif word == 'Right':
            list_buffer += 'Right'
        elif word == 'Up':
            list_buffer += 'Up'
        elif word == 'Down':
            list_buffer += 'Down'
        elif word == 'space-bar':
            list_buffer += ' '
        elif word == 'tab-key':
            list_buffer += 'Tab'
        elif word == 'Enter':
            list_buffer += 'Enter'
        elif word == 'page-up':
            list_buffer += 'PgUp'
        elif word == 'page-down':
            list_buffer += 'PgDn'
        elif word == 'Backspace':
            list_buffer += 'Backspace'
        elif word == 'delete':
            list_buffer += 'Del'
        elif word == 'escape':
            list_buffer += 'Esc'
        return list_buffer

    def get_mod(self, list_buffer, functional, word):
        if word == 'Shift':
            list_buffer += 'Shift'
        elif word == 'control-key':
            list_buffer += 'Ctrl'
        elif word == 'Alt':
            list_buffer += 'Alt'
        return list_buffer

    def get_nn(self, list_buffer, functional, word):
        list_buffer += self.convert_number_word(word)
        return list_buffer

    # 'Press' <special> <nn>
    def gotResults_5(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_special(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 3
        except Exception, e:
            handle_error('keys.vch', 36, '\'Press\' <special> <nn>', e)
            self.firstWord = -1

    # (('Left' | 'Right' | 'Up' | 'Down' | 'space-bar' | 'tab-key' | 'Enter' | 'page-up' | 'page-down' | 'Backspace' | 'delete' | 'escape')) <nn>
    def gotResults_28(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[0 + self.firstWord][0]
            if word == 'Left':
                top_buffer += 'Left'
            elif word == 'Right':
                top_buffer += 'Right'
            elif word == 'Up':
                top_buffer += 'Up'
            elif word == 'Down':
                top_buffer += 'Down'
            elif word == 'space-bar':
                top_buffer += ' '
            elif word == 'tab-key':
                top_buffer += 'Tab'
            elif word == 'Enter':
                top_buffer += 'Enter'
            elif word == 'page-up':
                top_buffer += 'PgUp'
            elif word == 'page-down':
                top_buffer += 'PgDn'
            elif word == 'Backspace':
                top_buffer += 'Backspace'
            elif word == 'delete':
                top_buffer += 'Del'
            elif word == 'escape':
                top_buffer += 'Esc'
            top_buffer += '_'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('keys.vch', 36, '((\'Left\' | \'Right\' | \'Up\' | \'Down\' | \'space-bar\' | \'tab-key\' | \'Enter\' | \'page-up\' | \'page-down\' | \'Backspace\' | \'delete\' | \'escape\')) <nn>', e)
            self.firstWord = -1

    # 'Press' <mod> <key> <nn>
    def gotResults_6(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[3 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 4
        except Exception, e:
            handle_error('keys.vch', 37, '\'Press\' <mod> <key> <nn>', e)
            self.firstWord = -1

    # ('Shift' | 'control-key' | 'Alt') <key> <nn>
    def gotResults_29(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[0 + self.firstWord][0]
            if word == 'Shift':
                top_buffer += 'Shift'
            elif word == 'control-key':
                top_buffer += 'Ctrl'
            elif word == 'Alt':
                top_buffer += 'Alt'
            top_buffer += '+'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 3
        except Exception, e:
            handle_error('keys.vch', 37, '(\'Shift\' | \'control-key\' | \'Alt\') <key> <nn>', e)
            self.firstWord = -1

    # 'Press' <mod> <mod> <key> <nn>
    def gotResults_7(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[3 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[4 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 5
        except Exception, e:
            handle_error('keys.vch', 38, '\'Press\' <mod> <mod> <key> <nn>', e)
            self.firstWord = -1

    # ('Shift' | 'control-key' | 'Alt') <mod> <key> <nn>
    def gotResults_30(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[0 + self.firstWord][0]
            if word == 'Shift':
                top_buffer += 'Shift'
            elif word == 'control-key':
                top_buffer += 'Ctrl'
            elif word == 'Alt':
                top_buffer += 'Alt'
            top_buffer += '+'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[3 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 4
        except Exception, e:
            handle_error('keys.vch', 38, '(\'Shift\' | \'control-key\' | \'Alt\') <mod> <key> <nn>', e)
            self.firstWord = -1

    # 'Press' <mod> <mod> <mod> <key> <nn>
    def gotResults_8(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[3 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[4 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[5 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 6
        except Exception, e:
            handle_error('keys.vch', 39, '\'Press\' <mod> <mod> <mod> <key> <nn>', e)
            self.firstWord = -1

    # ('Shift' | 'control-key' | 'Alt') <mod> <mod> <key> <nn>
    def gotResults_31(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{'
            word = fullResults[0 + self.firstWord][0]
            if word == 'Shift':
                top_buffer += 'Shift'
            elif word == 'control-key':
                top_buffer += 'Ctrl'
            elif word == 'Alt':
                top_buffer += 'Alt'
            top_buffer += '+'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[2 + self.firstWord][0]
            top_buffer = self.get_mod(top_buffer, False, word)
            top_buffer += '+'
            word = fullResults[3 + self.firstWord][0]
            top_buffer = self.get_key(top_buffer, False, word)
            top_buffer += '_'
            word = fullResults[4 + self.firstWord][0]
            top_buffer = self.get_nn(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 5
        except Exception, e:
            handle_error('keys.vch', 39, '(\'Shift\' | \'control-key\' | \'Alt\') <mod> <mod> <key> <nn>', e)
            self.firstWord = -1

    def get_n(self, list_buffer, functional, word):
        list_buffer += self.convert_number_word(word)
        return list_buffer

    # 'zoom' ('in' | 'out') <n>
    def gotResults_9(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            when_value = ''
            word = fullResults[2 + self.firstWord][0]
            when_value = self.get_n(when_value, True, word)
            if when_value != "":
                limit2 = ''
                word = fullResults[2 + self.firstWord][0]
                limit2 = self.get_n(limit2, True, word)
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    call_Dragon('Wait', 'i', [dragon3_arg1])
            else:
                limit2 = ''
                limit2 += '1'
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    call_Dragon('Wait', 'i', [dragon3_arg1])
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 3
        except Exception, e:
            handle_error('chrome.vcl', 9, '\'zoom\' (\'in\' | \'out\') <n>', e)
            self.firstWord = -1

    # 'zoom' ('in' | 'out')
    def gotResults_32(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            when_value = ''
            when_value += ''
            if when_value != "":
                limit2 = ''
                limit2 += ''
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    call_Dragon('Wait', 'i', [dragon3_arg1])
            else:
                limit2 = ''
                limit2 += '1'
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    call_Dragon('Wait', 'i', [dragon3_arg1])
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_32(words[2:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 9, '\'zoom\' (\'in\' | \'out\')', e)
            self.firstWord = -1

    # 'save'
    def gotResults_10(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+s}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_10(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 10, '\'save\'', e)
            self.firstWord = -1

    # 'new tab'
    def gotResults_11(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+t}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_11(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 11, '\'new tab\'', e)
            self.firstWord = -1

    # 'last'
    def gotResults_12(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+T}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_12(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 12, '\'last\'', e)
            self.firstWord = -1

    # 'new window'
    def gotResults_13(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+n}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_13(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 13, '\'new window\'', e)
            self.firstWord = -1

    # 'next' <n>
    def gotResults_14(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            word = fullResults[1 + self.firstWord][0]
            limit = self.get_n(limit, True, word)
            for i in range(to_long(limit)):
                top_buffer += '{Ctrl+tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('chrome.vcl', 14, '\'next\' <n>', e)
            self.firstWord = -1

    # 'previous' <n>
    def gotResults_15(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            word = fullResults[1 + self.firstWord][0]
            limit = self.get_n(limit, True, word)
            for i in range(to_long(limit)):
                top_buffer += '{Ctrl+Shift+tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('chrome.vcl', 15, '\'previous\' <n>', e)
            self.firstWord = -1

    # 'switch tab' <n>
    def gotResults_16(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl'
            top_buffer += '+'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_n(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('chrome.vcl', 16, '\'switch tab\' <n>', e)
            self.firstWord = -1

    # 'private'
    def gotResults_17(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+e}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '10'
            call_Dragon('Wait', 'i', [dragon_arg1])
            top_buffer += '{i}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_17(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 17, '\'private\'', e)
            self.firstWord = -1

    # 'close'
    def gotResults_18(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+w}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_18(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 18, '\'close\'', e)
            self.firstWord = -1

    # 'bookmark'
    def gotResults_19(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+d}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_19(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 19, '\'bookmark\'', e)
            self.firstWord = -1

    # 'tools'
    def gotResults_20(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+e}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_20(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 20, '\'tools\'', e)
            self.firstWord = -1

    # 'reload'
    def gotResults_21(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f5}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_21(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 21, '\'reload\'', e)
            self.firstWord = -1

    # 'back page'
    def gotResults_22(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{backspace}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_22(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 22, '\'back page\'', e)
            self.firstWord = -1

    # ('Copy' | 'Paste' | 'Go') ('Address' | 'URL')
    def gotResults_23(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+d}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            call_Dragon('Wait', 'i', [dragon_arg1])
            word = fullResults[0 + self.firstWord][0]
            if word == 'Copy':
                top_buffer += '{Ctrl+c}'
            elif word == 'Paste':
                top_buffer += '{Ctrl+v}'
            elif word == 'Go':
                top_buffer += ''
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_23(words[2:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 23, '(\'Copy\' | \'Paste\' | \'Go\') (\'Address\' | \'URL\')', e)
            self.firstWord = -1

    # 'text box'
    def gotResults_24(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'gi'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_24(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 25, '\'text box\'', e)
            self.firstWord = -1

    # 'show links'
    def gotResults_25(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'f'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_25(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 26, '\'show links\'', e)
            self.firstWord = -1

    # 'copy links'
    def gotResults_26(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'yf'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_26(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 29, '\'copy links\'', e)
            self.firstWord = -1

    # 'clear cash'
    def gotResults_27(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+del}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_27(words[1:], fullResults)
        except Exception, e:
            handle_error('chrome.vcl', 30, '\'clear cash\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
