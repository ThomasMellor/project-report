import plotting_functions as PF                                                                               
import glob                                                                                                   
import re                                                                                                     
import os                                                                                                     
import operator        
import fnmatch 

matches = []
for root, dirnames, filenames in os.walk('./gL_run_cL_one'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))
counter=0

lam = [[0,0],[0.2,0.2],[0.2,-0.2],[0.4,0.4],[0.4,-0.4],[0.6,-0.6],[0.6,0.6],[0.8,0.8],[0.8,-0.8],[1,1],[1,-1]]

colours = {40: 'red', 64: 'blue', 48: 'green', 128: 'orange', 72: 'gray', 104: 'black', 80: 'purple'}
sizes = [40,48, 64, 128, 72, 104,80 ]
dic = dict() 


for item in matches:
    print item 
for lambdas in lam:
    print lambdas
size_bool=False
with open('./gL_run_overlaid.tex','w') as main_file:
    with open('../project_code/tex_files/preamble.tex','r') as preable:
        for line in preable:
            main_file.write(line)
    prev_lam = 0
    for lambdas in lam:
        for path_file in matches:
            result = re.findall(r"-?\d+\.\d+|-?\d+", path_file)
            N=result[0]
	    dt=result[1]
 	    if(float(dt) != 0.01):
		continue
            if int(N) not in sizes:
                continue
            Lx=result[2]
            Ly=result[3]
            if float(Lx) != lambdas[0] or float(Ly) != lambdas[1]:
                continue
            cL=result[5]
            if float(cL)!= 0.2:
                continue
            itera=result[6]
            
            if(prev_lam != lambdas):
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
                    with open('./body_run.tex', 'r') as body:
                        for line in body:
                            main_file.write(line) 
            add_plot =  '\t\t\\addplot[only marks, mark=o, color= ' + colours[int(N)] + ', error bars/.cd, y dir = both, y explicit]\n'
            main_file.write(add_plot)
            table='\ttable[y error index=2]{' + path_file + '};\n'
            main_file.write(table)
            legend = '\\addlegendentry{$L=' + N +'$.}\n'  
            main_file.write(legend)
            prev_lam = lambdas 
    with open('../project_code/tex_files/end.tex','r') as end:
        for line in end:
            main_file.write(line)
    
    main_file.write('\\end{document}')
