# DocEasy

“DocEasy” is a software application developed with the intention of scanning text images and converting them into digitized editable documents using OCR technology. OCR also called Optical Character Reader is a system that provides a full alphanumeric recognition of printed or handwritten characters at electronic speed by simply scanning the form. The main purpose is to help the user to have an easy approach to scan any text and edit it with minimum hardware requirements. It maintains a high level of accuracy in recognizing the characters and all the documents scanned can be directly saved in our devices which can easily be accessed. The OCR technology used performs the tasks in less amount of time and more efficiently without the need to retype the document

**OCR Process:**

<img width="195" alt="image" src="https://github.com/CodeByTanya/DocEasy/assets/147076219/e59db614-fcf0-47ce-95af-c4b7f8efd56e">



**Product Features:**
We aim to make an application that converts handwritten documents into digitized format. We will integrate our additional features with the existing OCR-based technology Tesseract and release our product with the best user interface.
 Upon successful conversion, it lets the user specify which format he wants the output into like a .pptx, .docx, .xlsx, etc. 

| User action | DocEasy Response   |
| :---:   | :---: |
| Upload image | Store the image in the uploads folder   |
| Run OCR | Call the Pytesseract API to render text recognition   |
| Select extension | Select the required file extension   |
| Download image | Store the image in the downloads folder   |


The product has a simple and easy-to-understand structured flow. A clear target image with the least background details will act as an external input to the system. The system synchronizes with the internal logical files (upload directory) for image storage and retrieval. The image will be further passed on to the Pytesseract module for recognition of text, which will be displayed as an external output on the monitor screen. The system also synchronizes with the user’s downloads folder to download the file in the required extension specified by the user.


