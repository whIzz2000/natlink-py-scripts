# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.1I+, Sat Sep 13 18:23:35 2014

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <1> = ('next' | 'last' ) 'command' (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9) ;
        <any> = <1>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'pythonwin','')
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
        if   word == '0':
            return '0'
        else:
            return word

    # ('next' | 'last') 'command' 1..9
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            word = fullResults[2 + self.firstWord][0]
            limit += self.convert_number_word(word)
            for i in range(to_long(limit)):
                top_buffer += '{ctrl+'
                word = fullResults[0 + self.firstWord][0]
                if word == 'next':
                    top_buffer += 'j'
                elif word == 'last':
                    top_buffer += 'k'
                top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 3
            if len(words) > 3: self.gotResults_1(words[3:], fullResults)
        except Exception, e:
            handle_error('pythonwin.vcl', 4, '(\'next\' | \'last\') \'command\' 1..9', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
