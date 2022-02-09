#https://github.com/hyunwoongko/summarizers

from summarizers import Summarizers

def summarize_content(content):
    summ = Summarizers('normal')
    return summ(content) 
