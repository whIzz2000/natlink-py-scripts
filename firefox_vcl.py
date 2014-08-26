# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.1I+, Tue Aug 26 10:41:51 2014

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <1> = 'close' ;
        <2> = 'reload' ;
        <3> = 'firebug' ;
        <4> = 'remove all cookies' ;
        <18> = 'remove cookies' ;
        <n> = ('zero' | 'one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine') ;
        <5> = 'zoom' ('in' | 'out' ) <n> ;
        <19> = 'zoom' ('in' | 'out' ) ;
        <6> = 'save' ;
        <7> = 'new tab' ;
        <8> = 'last' ;
        <9> = 'new window' ;
        <10> = 'next' <n> ;
        <11> = 'previous' <n> ;
        <12> = 'close' ;
        <13> = 'bookmark' ;
        <14> = 'reload' ;
        <15> = 'back page' ;
        <16> = ('Copy' | 'Paste' | 'Go' ) ('Address' | 'URL' ) ;
        <17> = 'clear cash' ;
        <any> = <1>|<2>|<3>|<4>|<18>|<5>|<19>|<6>|<7>|<8>|<9>|<10>|<11>|<12>|<13>|<14>|<15>|<16>|<17>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'firefox','')
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

    # 'close'
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+w}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_1(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 2, '\'close\'', e)
            self.firstWord = -1

    # 'reload'
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+f5}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_2(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 3, '\'reload\'', e)
            self.firstWord = -1

    # 'firebug'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f12}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 4, '\'firebug\'', e)
            self.firstWord = -1

    # 'remove all cookies'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+o}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_4(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 6, '\'remove all cookies\'', e)
            self.firstWord = -1

    # 'remove cookies'
    def gotResults_18(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+o}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_18(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 6, '\'remove cookies\'', e)
            self.firstWord = -1

    def get_n(self, list_buffer, functional, word):
        list_buffer += self.convert_number_word(word)
        return list_buffer

    # 'zoom' ('in' | 'out') <n>
    def gotResults_5(self, words, fullResults):
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
            handle_error('firefox.vcl', 10, '\'zoom\' (\'in\' | \'out\') <n>', e)
            self.firstWord = -1

    # 'zoom' ('in' | 'out')
    def gotResults_19(self, words, fullResults):
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
            if len(words) > 2: self.gotResults_19(words[2:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 10, '\'zoom\' (\'in\' | \'out\')', e)
            self.firstWord = -1

    # 'save'
    def gotResults_6(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+s}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_6(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 11, '\'save\'', e)
            self.firstWord = -1

    # 'new tab'
    def gotResults_7(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+t}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_7(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 12, '\'new tab\'', e)
            self.firstWord = -1

    # 'last'
    def gotResults_8(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+T}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_8(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 13, '\'last\'', e)
            self.firstWord = -1

    # 'new window'
    def gotResults_9(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+n}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_9(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 14, '\'new window\'', e)
            self.firstWord = -1

    # 'next' <n>
    def gotResults_10(self, words, fullResults):
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
            handle_error('firefox.vcl', 15, '\'next\' <n>', e)
            self.firstWord = -1

    # 'previous' <n>
    def gotResults_11(self, words, fullResults):
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
            handle_error('firefox.vcl', 16, '\'previous\' <n>', e)
            self.firstWord = -1

    # 'close'
    def gotResults_12(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+w}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_12(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 17, '\'close\'', e)
            self.firstWord = -1

    # 'bookmark'
    def gotResults_13(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+d}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_13(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 18, '\'bookmark\'', e)
            self.firstWord = -1

    # 'reload'
    def gotResults_14(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f5}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_14(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 19, '\'reload\'', e)
            self.firstWord = -1

    # 'back page'
    def gotResults_15(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{backspace}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_15(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 20, '\'back page\'', e)
            self.firstWord = -1

    # ('Copy' | 'Paste' | 'Go') ('Address' | 'URL')
    def gotResults_16(self, words, fullResults):
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
            if len(words) > 2: self.gotResults_16(words[2:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 21, '(\'Copy\' | \'Paste\' | \'Go\') (\'Address\' | \'URL\')', e)
            self.firstWord = -1

    # 'clear cash'
    def gotResults_17(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+del}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_17(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 22, '\'clear cash\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
