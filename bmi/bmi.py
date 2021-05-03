import sys
<<<<<<< HEAD:bmi.py



def ounces2pounds(x):
    return x/16

=======
>>>>>>> dev:bmi/bmi.py
def stones2pounds(x):
    return x*14
    
def ounces2pounds(x):
    return x/16
    
def inches2feet(x):
    return x/12


def weight2kg(stones,pounds,ounces):
    kg = (stones2pounds(stones)+pounds+ounces2pounds(ounces))/2.2
    return kg

def height2metres(feet,inches):
<<<<<<< HEAD:bmi.py
    return feet/3.28
=======
    metre = (feet+inches2feet(inches))/3.28
    return metre
>>>>>>> dev:bmi/bmi.py


def categorise(kg,metre):
    bmi=kg/(metre*metre)
    if bmi<19:
        cat='A'
    elif bmi<=26:
        cat='B'
    elif bmi<=30:
        cat='C'
    else:
        cat='D'
    return cat

def get_data(input_file):
    f=open(input_file)
    data=[]
    for line in f:
        person_id,stones,pounds,ounces,feet,inches=line.split()
        kg=weight2kg(int(stones),int(pounds),int(ounces))
        m =height2metres(int(feet),int(inches))
        cat=categorise(kg,m)
        data.append((person_id,cat))
    f.close()
    return data
        
    
def convert(input_file,output_file):
    data = get_data(input_file)
    g=open(output_file,"w")
    for (person_id,cat) in data:
        g.write("%s\t%s\n"%(person_id,cat))
    g.close()


if __name__ == "__main__":
    convert(sys.argv[1],sys.argv[2])

    
