#Claire Trebing 
#Repo: GridWorld
#Concept: Q-Learning 
import agentClass

def MapPrettyPrint(map):
	for line in map:
		print(line)
	return

#Hard Code the map into the program
basementMap = [[0 for x in range(10)] for y in range(10)]
basementMap[0] = ['W','W','W','W','W','W','W','W','W','W']
basementMap[1] = ['W','_','_','T','_','_','_','_','_','W']
basementMap[2] = ['W','_','W','_','W','W','W','T','_','W']
basementMap[3] = ['W','_','W','_','T','_','_','_','_','W']
basementMap[4] = ['W','_','W','_','_','_','W','_','_','W']
basementMap[5] = ['W','_','T','_','_','_','W','_','_','W']
basementMap[6] = ['W','_','_','_','W','T','W','T','_','W']
basementMap[7] = ['W','_','T','_','W','_','_','_','_','W']
basementMap[8] = ['W','_','_','_','W','_','_','_','_','W']
basementMap[9] = basementMap[0]

MapPrettyPrint(basementMap)

#Begin main
#if __name__ == '__main__':