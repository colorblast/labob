#! /usr/bin/python

import cgi

import cgitb
cgitb.enable()

#HTML_HEADER = 'Content-type: text/html'

import os
import tempfile

userInput = cgi.FieldStorage()
docFormat = userInput['format'].value
author = userInput['authname'].value
title = userInput['title'].value
date =  userInput['date'].value
starter = userInput['starter'].value
starterText = userInput['starterText'].value
bodyText = userInput['body'].value
fxn = userInput['function'].value
landscape = userInput['landscape'].value



latexc = tempfile.NamedTemporaryFile()
#try:
#    print 'temp:', temp
#    print 'temp.name:', temp.name

# Document Formatting Changes:
if starter="Standard (recommended)":
	articleclass="article"
if starter="Turabian":
	## ADD NEW QUERY
if starter="APA":
	articleclass="apa"
if starter="MLA":
	mla="\begin{mla}{"fname"}{"lname"}{"Plname"}{"Classname"}{\today}{Really Cool Title}"
if not starter="MLA":
	mla=""
#Landscaping:
if landscape=True:
	lsss=""
else:
	lsss="%"

lbasic='''
\documentclass[11pt, oneside]{'''articleclass'''}   	% use "amsart" instead of "article" for AMSLaTeX format
\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
\geometry{letterpaper}                   		% ... or a4paper or a5paper or ... 
'''lsss'''\geometry{landscape}                		% Activate for rotated page geometry
%\usepackage[parfill]{parskip}    		% Activate to begin paragraphs with an empty line rather than an indent
\usepackage{graphicx}				% Use pdf, png, jpg, or epsÂ§ with pdflatex; use eps in DVI mode
								% TeX will automatically convert eps --> pdf in pdflatex		
\usepackage{amssymb}

%SetFonts

%SetFonts


\title{'''+title'''}
\author{'''+author+'''}
\date{'''+date+'''}							% Activate to display a given date or no date

\begin{document}
\maketitle
%\section{}
%\subsection{}



\end{document}  	
'''
finally:
    # Automatically cleans up the file
    latexc.close()
# print 'Exists after close:', os.path.exists(temp.name)




def main():
	#print HTML_HEADER
	#print HEAD
	#print END
main()
