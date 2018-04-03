# extractPDF
Minimal Python utility for breaking a single PDF into multiple smaller PDF based on start and end page indices

Developed for breaking NSF and NIH grant proposals written in LaTeX into separate documents, though there are many other applications

# Usage - Single File
Assuming you have a 39 page PDF entitled `research_strategy.pdf`:  
`chmod +x extractPDF.py`  
`./extractPDF.py --input research_strategy.pdf --output cover_letter.pdf --start 3 --end 3`


# Usage - Multiple Files  
Assuming you have a 39 page PDF entitled `research_strategy.pdf`; the .sh file just has a bunch of calls to extractPDF.py  
`chmod +x extractPDF.py` 
`chmod +x extractIndividualComponents.sh`   
`./extractIndividualComponents.sh`  


