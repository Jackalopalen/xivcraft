import os

#this is PART of the function used to convert the lists of recipes acquired from ashley sss into something useful
for rlist in os.listdir('Recipes'):
	rc = 0
	cc += 1
	rclass = rlist.replace('.txt','')
	f = open('./Recipes/{}'.format(rlist),'r')
	st = f.read()
	f.close()
	st = re.sub('Recipi*es.*\n','',st)
	sl = re.split('\n *\n',st)
	for recipe in sl:
		rc += 1
		print "class {} recipe {}".format(cc,rc)
		rl = recipe.split('\n')
		nl = rl.pop(0)
		nl = nl.split(' (Level ')
		name = nl[0]
		level = int(nl[1].rstrip().rstrip(')'))
		rl = [g.lstrip() for g in rl]
		ingredients = []
		for ing in rl:
			il = ing.split(' ',1)
			ingredients.append((il[1],eval(il[0])))
		Recipes.append({'Name':name,'Class':rclass,'Level':level,'Ingredients':ingredients})
