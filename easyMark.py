## Python code for testing and developing easyMark
def easyMarkOLD(string):
	for x in range(len(string)):
		if string[x]=="~":
			# Making Lists:
			if string[x:x+11]=="~start-list":
				string=string[:x]+r"\begin{enumerate}"+string[x+11:]
			if string[x:x+9]=="~end-list":
				string=string[:x]+r"\end{enumerate}"+string[x+9:]
			if string[x:x+2]=="~ ":
				string=string[:x]+r"\item "+string[x+2:]
			if string[x:x+14]=="~start-bullets":
				string=string[:x]+r"\begin{itemize}"+string[x+14:]
			if string[x:x+12]=="~end-bullets":
				string=string[:x]+r"\end{itemize}"+string[x+12:]
			if string[x:x+18]=="~start-custom-list":
				string=string[:x]+r"\begin{description}"+string[x+18:]
			if string[x:x+16]=="~end-custom-list":
				string=string[:x]+r"\end{description}"+string[x+16:]
			# Structuring Your Paper:
			if string[x:x+10]=="~chapter [":
				yandexf=string.find("]", x+10)
				string=string[:x]+r"\chapter{"+string[x+10:yandexf]+"}"+string[yandexf+1:]
			# Note: Raw strings added, but it is better to check them.
	return(string)

def easyMark(string):
        # Making Lists:
        out=string.replace("~start-list", r"\begin{enumerate}")
        out=out.replace("~end-list", r"\end{enumerate}")
        out=out.replace("~ ", r"\item ")
        out=out.replace("~start-bullets", r"\begin{itemize}")
        out=out.replace("~end-bullets", r"\end{itemize}")
        out=out.replace("~start-custom-list", r"\begin{description}")
        out=out.replace("~end-custom-list", r"\end{description}")
        # Document Structure:
        while out.find("~chapter")!=-1:
                popper=False
                yandex=out.find("~chapter [")
                if yandex==-1:
                        yandex=out.find("~chapter[")
                        if yandex!=-1:
                                popper=True
                        if yandex==-1:
                                popper='solo'
                        #out=out.replace("~chapter", r"<<SYNTAX ERROR: Improper Usage>>")
                        #break
                bing=out.find("]", yandex)
                if bing==-1 and popper!='solo':
                        out=out.replace("~chapter", r"<<SYNTAX ERROR: Improper Document Structure Usage>>")
                        break
                if popper==False:
                        out=out[:yandex]+out[yandex:bing].replace("~chapter [", r"\chapter{")+"}"+out[bing+1:]
                if popper==True:
                        out=out[:yandex]+out[yandex:bing].replace("~chapter[", r"\chapter{")+"}"+out[bing+1:]
                if popper=='solo':
                        out=out.replace("~chapter",r"\chapter{}")
        while out.find("~section")!=-1:
                popper=False
                yandex=out.find("~section [")
                if yandex==-1:
                        yandex=out.find("~section[")
                        if yandex!=-1:
                                popper=True
                        if yandex==-1:
                                popper='solo'
                        #out=out.replace("~section", r"<<SYNTAX ERROR: Improper Usage>>")
                        #break
                bing=out.find("]", yandex)
                if bing==-1 and popper!='solo':
                        out=out.replace("~section", r"<<SYNTAX ERROR: Improper Document Structure Usage>>")
                        break
                if popper==False:
                        out=out[:yandex]+out[yandex:bing].replace("~section [", r"\section{")+"}"+out[bing+1:]
                if popper==True:
                        out=out[:yandex]+out[yandex:bing].replace("~section[", r"\section{")+"}"+out[bing+1:]
                if popper=='solo':
                        out=out.replace("~section",r"\section{}")
        while out.find("~subsection")!=-1:
                popper=False
                yandex=out.find("~subsection [")
                if yandex==-1:
                        yandex=out.find("~subsection[")
                        if yandex!=-1:
                                popper=True
                        if yandex==-1:
                                popper='solo'
                        #out=out.replace("~subsection", r"<<SYNTAX ERROR: Improper Usage>>")
                        #break
                bing=out.find("]", yandex)
                if bing==-1 and popper!='solo':
                        out=out.replace("~subsection", r"<<SYNTAX ERROR: Improper Document Structure Usage>>")
                        break
                if popper==False:
                        out=out[:yandex]+out[yandex:bing].replace("~subsection [", r"\subsection{")+"}"+out[bing+1:]
                if popper==True:
                        out=out[:yandex]+out[yandex:bing].replace("~subsection[", r"\subsection{")+"}"+out[bing+1:]
                if popper=='solo':
                        out=out.replace("~subsection",r"\subsection{}")
        while out.find("~subsubsection")!=-1:
                popper=False
                yandex=out.find("~subsubsection [")
                if yandex==-1:
                        yandex=out.find("~subsubsection[")
                        if yandex!=-1:
                                popper=True
                        if yandex==-1:
                                popper='solo'
                        #out=out.replace("~subsubsection", r"<<SYNTAX ERROR: Improper Usage>>")
                        #break
                bing=out.find("]", yandex)
                if bing==-1 and popper!='solo':
                        out=out.replace("~subsubsection", r"<<SYNTAX ERROR: Improper Document Structure Usage>>")
                        break
                if popper==False:
                        out=out[:yandex]+out[yandex:bing].replace("~subsubsection [", r"\subsubsection{")+"}"+out[bing+1:]
                if popper==True:
                        out=out[:yandex]+out[yandex:bing].replace("~subsubsection[", r"\subsubsection{")+"}"+out[bing+1:]
                if popper=='solo':
                        out=out.replace("~subsubsection",r"\subsubsection{}")
        # Visual Breaks:
        out=out.replace("~hoz-line-break", r"\hrulefill")
        out=out.replace("~new-page", r"\clearpage")
        return(out)
