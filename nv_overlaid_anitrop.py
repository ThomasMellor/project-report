import plotting_functions as PF                                                                               
import glob                                                                                                   
import re                                                                                                     
import os                                                                                                     
import operator        
import fnmatch 

matches = []
for root, dirnames, filenames in os.walk('../project_code/nv_log'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))
counter=0

lam = [[0,0],[0.2,-0.2],[0.4,-0.4],[0.6,-0.6],[0.8,-0.8],[1,-1],[1.5,-1.5],[2,-2]]

colours = {0: 'red', 0.2: 'blue', 0.4: 'green', 0.6: 'orange',0.8: 'gray', 1: 'black', 1.5: 'purple', 2: 'yellow'}
sizes = [40,48, 64, 128, 104, 72 ,80, 512 ]
dic = dict() 
for path_file in matches:
    result = re.findall(r"-?\d+\.\d+|-?\d+", path_file)
    N=result[0]
    dt=result[1]
    Lx=result[2]
    Ly=result[3]
    run=result[5]
    cL=result[6]
    itera=result[7]
    key = N + ',' + dt + ',' + Lx + ',' + Ly + ',' + cL + ',' + itera
    if key not in dic:
        dic[key] = int(run)
    if key in dic:
        if int(run) > dic[key]:
            dic[key] = int(run)

size_bool = False 


with open('./nv_overlaid_anistropic.tex','w') as main_file:
    with open('../project_code/tex_files/preamble.tex','r') as preable:
        for line in preable:
            main_file.write(line)
    prev_size = -1
    for size in sizes:
        for path_file in matches:
            result = re.findall(r"-?\d+\.\d+|-?\d+", path_file)
            if( int(result[4]) == 2 or int(result[4]) == 4):
                continue 
            N=result[0]
	    dt=result[1]
            if int(N) !=  size:
                continue
            Lx=result[2]
            Ly=result[3]
            if [float(Lx), float(Ly)] not in lam:
                continue
            run=result[5]
            cL=result[6]
            if float(cL)!= 0.2:
                continue
            itera=result[7]
            exp=result[8]
	    err=result[9]
            key = N +  ','+ dt+ ','+ Lx + ',' + Ly + ',' + cL + ',' + itera
            if dic[key] != int(run):
                continue
            
            if(prev_size != size):
                if(size_bool == True):
                    with open('../project_code/tex_files/end.tex','r') as end:
                        for line in end:
                            main_file.write(line)
                else:
                    size_bool = True
                counter+=1
            
                if(counter==3):
                    main_file.write('\\clearpage\n')
                    counter=0
                with open('../project_code/tex_files/begin.tex','r') as begin:
                    for line in begin:
                        main_file.write(line) 
                    title = '\t\ttitle={Vortices  for  N = $' + N + '$.},\n' 
                    main_file.write(title)
                    with open('../project_code/tex_files/body_nv_overlaid.tex', 'r') as body:
                        for line in body:
                            main_file.write(line) 
            add_plot =  '\t\t\\addplot[mark=none, color= ' + colours[float(Lx)] +']\n'
            main_file.write(add_plot)
            table='\ttable{' + path_file + '};\n'
            main_file.write(table)
            legend = '\\addlegendentry{$\lambda_x = ' + Lx + '$, exp $=' + exp + '\\pm' + err + '$,\\\\ realisations = ' + run + '}\n'  
            main_file.write(legend)
            prev_size = size 
    with open('../project_code/tex_files/end.tex','r') as end:
        for line in end:
            main_file.write(line)
    
    main_file.write('\\end{document}')
