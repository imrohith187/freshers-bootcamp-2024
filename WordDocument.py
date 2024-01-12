from abc import ABC, abstractmethod

class DocumentPart(ABC):
    @abstractmethod
    def paint(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
class WordDocument(DocumentPart):
    def save(self):
        print("Word Document Saved")
    
    def open(self):
        print("Word Document Opened")
        
class Header(DocumentPart):
    def __init__(self,documentTitle):
        self.documentTitle = documentTitle
    
    def paint(self):
        print("Header Paint")
    
    def save(self):
        print("Header Saved")

class Paragraph(DocumentPart):
    def __init__(self,paraContent):
        self.paraContent = paraContent
    
    def paint(self):
        print("Paragraph Paint")
    
    def save(self):
        print("Paragraph Saved") 
        
class Hypertext(DocumentPart):
    def __init__(self,hyperlink):
        self.hyperlink = hyperlink
    
    def paint(self):
        print("Hypertext Paint")
    
    def save(self):
        print("Hypertext Saved") 
        
h=Paragraph("www")
h.paint()

def main():
    header = Header()
    footer = Footer()
    hyperlink = Hypertext()
    paragraph = Paragraph()
    word_doc = WordDocument([header, footer, hyperlink, paragraph])
    word_doc.paint_all()
    word_doc.save_all()
if __name__ == "__main__":
    main()
        
