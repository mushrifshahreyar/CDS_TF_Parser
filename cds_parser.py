from os import name
import sys
import xlsxwriter
import re


def parser(fname = 'cds_output.xlsx'):
    # change the output file name
    excel_workbook = xlsxwriter.Workbook(fname)
    worksheet_parameters = excel_workbook.add_worksheet('parameter')
    worksheet_components = excel_workbook.add_worksheet('component')
    worksheet_associations = excel_workbook.add_worksheet('association')

    count_comp = 0
    count_assoc = 0
    total_component = 0
    is_component = False
    
    Lines = []
    file1 = open("cdsview.txt","r")
    Lines = file1.readlines()
    t_Lines = Lines
    regex = re.compile('[@!#$%^&\'*()<>?/\|}{~:.]')
    is_parameter = False
    p_count = 0

    # Reading parameters
    for line in t_Lines:
        if 'with parameters' in line:
            is_parameter = True
            continue
        if 'as select from' in line:
            is_parameter = False

        if(is_parameter):
            if ':' in line:
                words = line.split()
                for i,w in enumerate(words):
                    if w == ':':
                        worksheet_parameters.write(p_count,0,words[i-1])
                        worksheet_parameters.write(p_count,1,words[i+1].upper())
                        p_count += 1

    for line in Lines:
        # checing main block for components
        if '{' in line:
            is_component = True
            total_component += 1

        if '}' in line:
            total_component -= 1
            if total_component == 0:
                is_component = False
        
        if is_component:
            if(len(line) > 1):
                # checking for ',' in line
                if(line[-2] == ','):
                    ws = line.split()
                    # getting last word from the line
                    w = ws[len(ws)-1]
                    
                    # checking for special character in the word
                    if(regex.search(w) == None):
                        if(',' in w):
                            if('_' in w):
                                if(w.find('_') != 0):
                                    w = w.replace(',','')
                                    worksheet_components.write(count_comp,0,w)
                                    count_comp += 1
                            else:
                                w = w.replace(',','')
                                worksheet_components.write(count_comp,0,w)
                                count_comp += 1
        
        # Reading associations
        if 'as' in line:
            words = line.split()
            if 'association' in words:
                for i,w in enumerate(words):
                    if w == 'as':
                        worksheet_associations.write(count_assoc,0,words[1])
                        worksheet_associations.write(count_assoc,1,words[i-1])
                        worksheet_associations.write(count_assoc,2,words[i+1])
                        count_assoc += 1
        
        
    excel_workbook.close()

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        parser(sys.argv[1])
    else:
        parser()

        