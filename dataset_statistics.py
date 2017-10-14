# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para gerar estatísticas de um conjunto de redes-ego
## 
######################################################################################################################################################################

def statistics(dataset_dir,output_dir):
	print("\n######################################################################\n")
	print ("Dataset statistics - " +str(dataset_dir))
	
	nodes = 0
	edges = 0
	i=0
	for file in os.listdir(dataset_dir):
		i+=1
		G = snap.LoadEdgeList(snap.PNGraph, dataset_dir+file, 0, 1)							   # load from a text file
		nodes = nodes+G.GetNodes()
		edges = edges+G.GetEdges()

#		for NI in G.Nodes():
			#NI.GetOutDeg(), NI.GetInDeg())			#"out-degree - in-degree
			#NI.GetId())						#"node id - 
		print ("EGO %d ----- Nodes: %d -----  Edges %d" % (i,G.GetNodes(), G.GetEdges()))
	

	print("######################################################################")
	print("Nodes	"+str((nodes)))
	print("Edges	"+str((edges)))
	print 
	print

#Nodes	81306
#Edges	1768149
#Nodes in largest WCC	81306 (1.000)
#Edges in largest WCC	1768149 (1.000)
#Nodes in largest SCC	68413 (0.841)
#Edges in largest SCC	1685163 (0.953)
#Average clustering coefficient	0.5653
#Number of triangles	13082506
#Fraction of closed triangles	0.06415
#Diameter (longest shortest path)	7
#90-percentile effective diameter	4.5

#Dataset			N				E				C				K				S				A
#Twitter			125,120		2,248,406	3,140			33,569		15.54			0.39

#DATASET STATISTICS.
#N: NUMBER OF NODES,
#E: NUMBER OF EDGES,
#C: NUMBER OF COMMUNITIES,
#K: NUMBER OF NODE ATTRIBUTES,
#S: AVERAGE COMMUNITY SIZE,
#A: COMMUNITY MEMBERSHIPS PER NODE
print("\n######################################################################\n")

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" Script para apresentação de statísticas do dataset (rede-ego)							"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - Follow"
	print"  9 - Follwowers"
	print"  2 - Retweets"
	print"  3 - Likes"
	print"  3 - Mentions"
	
	print " "
	print"  5 - Co-Follow"
	print" 10 - Co-Followers"				
	print"  6 - Co-Retweets"
	print"  7 - Co-Likes"
	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))
	net = "n"+str(op)	
	dataset_dir = "/home/amaury/graphs/"+str(net)+"/graphs_with_ego/"								############### Arquivo contendo arquivos com a lista de arestas das redes-ego
	dataset_dir = "/home/amaury/snappy/twitter/edges/"								#Testes... REMOVER DEPOIS!

	if not os.path.isdir(dataset_dir):
		print("Diretório dos grafos não encontrado: "+str(dataset_dir))
		print("Saindo...")
		sys.exit()
	else:
		output_dir = "/home/amaury/Dropbox/statistics/"+str(net)+"/graphs_with_ego/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)	
		statistics(dataset_dir,output_dir)	

	print("\n######################################################################\n")
	print("Coleta finalizada!")
	print("\n######################################################################\n")

############################################
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################



######################################################################################################################


#Executa o método main
if __name__ == "__main__": main()