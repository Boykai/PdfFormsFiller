__author__ = 'toolesiij'
import fields as funcs

def main():
    pdf_path = 'rando.pdf'
    fields = funcs.get_fields(pdf_path)
    fields['name' 'telephone'] = 'James'
    fields['telephone'] = '4077299999'
    funcs.write_pdf(pdf_path, fields, 'output.pdf')


if __name__ == '__main__':
    main()




