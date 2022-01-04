import xlsxwriter
import sys

def parser(fname = 'tf_output.xlsx'):
    count = 0
    Lines = []
    file1 = open("tf.txt","r")
    excel_workbook = xlsxwriter.Workbook(fname)
    worksheet_parameters = excel_workbook.add_worksheet('parameter')
    worksheet_components = excel_workbook.add_worksheet('component')
    
    Lines = file1.readlines()
    naming = []
    n = True
    t_Lines = Lines
    p_count = 0
    is_parameter = False
    for line in t_Lines:
        if 'with parameters' in line:
            is_parameter = True
        if 'returns' in line:
            is_parameter = False
        if is_parameter:
            if ':' in line:
                words = line.split()
                for i,w in enumerate(words):
                    if w == ':':
                        worksheet_parameters.write(count,0,words[i-1])
                        worksheet_parameters.write(count,1,words[i+1].upper())
                        p_count += 1

    for line in Lines:
        if ':' in line:
            words = line.split()
            for i,w in enumerate(words):
                if w == ':':
                    if(';' in words[i+1]):
                        words[i+1] = words[i+1].replace(';','')
                        worksheet_components.write(count,0,words[i-1])
                        worksheet_components.write(count,1,words[i+1].upper())
                        count += 1
    excel_workbook.close()

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        parser(sys.argv[1])
    else:
        parser()
