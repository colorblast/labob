## Python code for testing and developing easyMark
def easyMark(string):
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
