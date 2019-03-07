
# Warning: make sure to use commit: 9c1fd27 from https://github.com/Jean-Baptiste-Camps/Geste 
import os
import random
random.seed(1001)

root = './Geste/'

# files = [f for f in os.listdir(root) if f.endswith('csv')]
files = ['transcr_Asprem_P4_pos.csv', 'transcr_Otin_B_pos.csv', 'transcr_Asprem_C_pos.csv', 'transcr_Fier_V_pos.csv', 'ed_GuiBourgG_pos.csv', 'transcr_Otin_M_pos.csv', 'ed_FloovG_pos.csv', 'transcr_Otin_A_pos.csv']

random.shuffle(files)


def subsets(nsents=100):
    subsets = []
    for f in files:
        subset = []
        with open(os.path.join(root, f)) as f:
            sent = []
            for line in f:
                if len(subset) == nsents:
                    subsets.append(subset)
                    subset = []
                if not line.strip():
                    sent.append("\n")
                    subset.append(sent)
                    sent = []
                else:
                    sent.append(line)

    if subset:
        subsets.append(subset)

    return subsets


subsets = subsets()
five, ten = round(len(subsets) * 0.05), round(len(subsets) * 0.1)
random.shuffle(subsets)


def writesubsets(path, subsets):
    with open(path, 'w') as f:
        f.write("token\tlemma\tpos\tmorph\n")
        for subset in subsets:
            for sent in subset:
                for line in sent:
                    f.write(line)


target = 'corpus'
if not os.path.isdir(os.path.join(root, target)):
    os.makedirs(os.path.join(root, target))
for split, subsets in {
    'dev': subsets[:five],
    'test': subsets[five:five+ten],
    'train': subsets[five+ten:]
}.items():
    writesubsets(os.path.join(root, target, '{}.tsv'.format(split)), subsets)
