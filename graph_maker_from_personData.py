### c:\Python27\python -u -i $(FULL_CURRENT_PATH)
import json, os


os.chdir("c:\\py\\")

f = open("persons_831.json")
data = json.loads(f.read())
f.close()

skills = {}
n = len(data)
MIN_COUNT = 12
MIN_EDGE_COUNT = 10

for person in data[:n]:
	for s in person['skills']:
		if s['skill'].lower() not in skills.keys(): skills[s['skill'].lower()] = 1
		else: skills[s['skill'].lower()] += 1

	
edges = {}
i = 0
for person in data[:n]:
	print i
	i+= 1
	for s1 in person['skills']:		
		for s2 in person['skills']:
			skill1 = s1['skill'].lower()
			skill2 = s2['skill'].lower()
			if (skill2, skill1) in edges :
				t = skill1
				skill1 = skill2
				skill2 = skill1
			if (skill1, skill2) not in edges : edges[(skill1, skill2)] = 1
			else :	edges[(skill1, skill2)] += 1


skills_ = [s for s in skills if skills[s] >= MIN_COUNT]
skills_dict = [{'name': s, 'count' : skills[s]} for s in skills_]
edges_ = [{'source': skills_.index(s), 'target' : skills_.index(t), 'count' : edges[(s,t)]} for (s, t) in edges if (skills[t] >= MIN_COUNT and skills[s] >= MIN_COUNT and edges[(s,t)] >= MIN_EDGE_COUNT)] #if (skills[s] > MIN_COUNT and skills[t] > MIN_COUNT)



mygraph = {'nodes' : skills_dict, 'edges' : edges_}

out = open('myGraph_831.json', 'w')
print >>out, json.dumps(mygraph, sort_keys = True, indent = 4)
out.close()

print 'nodes:', len(mygraph['nodes'])
print 'edges:', len(mygraph['edges'])
print 'size:', len(json.dumps(mygraph, sort_keys = True, indent = 4))

			

			


		
