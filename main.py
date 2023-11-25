from PyPDF2 import PdfReader
# from tabula import read_pdf
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.pdf'):
            process_pdf(event.src_path)

def process_pdf(bank_statement):
    pdf_file = open(bank_statement, 'rb')
    reader = PdfReader(pdf_file)

    account_activity_page_1 = 2
    # account_activity_page_2 = 3
    num_of_transactions = 0
    amount = 0

    page1 = reader.pages[account_activity_page_1]
    text = page1.extract_text()
    lines1 = text.split('\n')

    for line in lines1:
        row = line.split()
        if '/' in row[0] and len(row[0]) == 5 and row[1] != 'Payment':
            # print(row)
            num_of_transactions += 1
            amount += float(row[-1])

    print(f"Number of transactions: {num_of_transactions}")
    print(f"Amount: ${amount}")

if __name__ == "__main__":
    folder_to_watch = './statements'
    event_handler = PDFHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)

    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
