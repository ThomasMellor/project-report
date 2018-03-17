import math

def graph_points(file_name):
    graph = []
    with open(file_name,'r') as doc:                         
        for line in doc.readlines():
            l = line.strip().split(' ')
            graph.append([float(l[0]), float(l[1])])
    return graph 

def write_file(file_name, data):
    with open(file_name,'w') as doc:
        for l in data:
            doc.write(str(l[0]))
            doc.write(' ')
            doc.write(str(l[1]))
            doc.write('\n')

def append_file(file_name, data):
    with open(file_name, 'a+') as doc:
        for l in data:
            for i in range(len(l)):
	        doc.write(str(l[i]))                                                                             
                doc.write(' ')
	    doc.write('\n')                                                                                   
			
def error_graph(mag2_graph, mag4_graph, N) :
    error_graph = []
    for i in range(len(mag2_graph)) :
	error_mag = mag4_graph[i][1]-pow(mag2_graph[i][1],2)
	err = 2*math.sqrt(float(4)/(N-1)*error_mag*(mag4_graph[i][1]/pow(mag2_graph[i][1],4)  + pow(mag4_graph[i][1],2)/pow(mag2_graph[i][1],6)-2*mag4_graph[i][1]/pow(mag2_graph[i][1],4)))
	error_graph.append([mag2_graph[i][0], err])
    return error_graph 	


def normalise(f1, f2, graph):
    for point in graph:
        point[0] = f1(point[0])
        point[1] = f2(point[1])
    return graph

def div_log(t):
    return t/math.log(t)

def log_div_log(t):
    return math.log(div_log(t))

def subset_graph(x1, x2, graph):
    subset = []
    for point in graph:
        if point[0] > x1 and point[0] < x2:
            subset.append(point)
    return subset

def split_graph(first, second, graph):
    for point in graph:
        first.append(point[0])
        second.append(point[1])

def gr_n(graph, n):
    gr_n_graph = []
    for point in graph:
        if point[0] > n:
            gr_n_graph.append(point)
    return gr_n_graph

def gr_n_2(graph, n):
    gr_n_graph = []
    for point in graph:
        if point[1] > n:
            gr_n_graph.append(point)
    return gr_n_graph
