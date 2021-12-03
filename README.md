# extractPDF
Minimal Python utility for breaking a single PDF into multiple smaller PDF based on start and end page indices. It uses the PyPDF2 library for pdf reading and writing.

Developed for breaking NSF and NIH grant proposals written in LaTeX / Overleaf into separate documents for submission, though there are many other applications

# Usage - Single Output File
Assuming you have a 39 page PDF entitled `research_strategy.pdf`:  
`python3 extractPDF.py --input research_strategy.pdf --output cover_letter.pdf --start 3 --end 3`


# Usage - Multiple Files  
Assuming you have a 39 page PDF entitled `research_strategy.pdf`; the .sh file just has a bunch of calls to extractPDF.py  
`chmod +x extractIndividualComponents.sh`   
`./extractIndividualComponents.sh`  
