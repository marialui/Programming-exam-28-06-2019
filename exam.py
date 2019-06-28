#define a function that takes a list as anput and return the maximum value of the list ant its position
def Max_list_position(lista):
    max=lista[0]
    pos=0
    for i in range(len(lista)):
        if lista[i]> max:
            max=lista[i]
            pos=i
    return[max,pos]

#define a function that will return the best probability among all the transitions, and its position
def best_transition(i,j,states,V,trans_p):
    l=[]
    for k in range(len(states)):
        contribute= V[k][j-1]*trans_p[k][i]
        l.append(contribute)
    best= Max_list_position(l)
    return best #best will be a list containing the max probability and its position

def Preatty_Matrix(M):
    for row in M:
        line=''
        for el in row:
            line=line +str(el)+ '\t'
        print('%s \n' %(line))


def Viterbi(sq, states, trans_p, emiss_p, emiss_ind):
    sq = '-' + sq + '-'
    # add 2 extracharaters
    V = [['*' for j in range(len(sq))] for i in range(len(states))]
    P = [['*' for j in range(len(sq))] for i in range(len(states))]
    # Initialise the probability matrix (V)
    V[0][0] = 1
    for i in range(1, len(states)):
        V[i][0] = 0
    # fill the probability and the pointer matrix
    for j in range(1, len(sq) - 1):
        sq_char = sq[j]
        for i in range(len(states)):
            best_prob = best_transition(i, j, states,V, trans_p)
            V[i][j] = best_prob[0] * emiss_p[i][emiss_ind[sq_char]]
            P[i][j] = best_prob[1]
    # termination
    last_transition = best_transition(len(states) - 1, len(sq) - 1, states,V, trans_p)
    V[len(states) - 1][len(sq) - 1] = last_transition[0]
    P[len(states) - 1][len(sq) - 1] = last_transition[1]
#la funzione restituisce la probability matrix e la pointer matrix
    return [V, P] #the p(s|m) will be the last cell of the probability matrix --> V[len(states) - 1][len(sq) - 1]

#given the pointer matrix and the states compute the path
#sq is the sequence without the 2 extracharacter

def Traceback(states,P, sq):
    I = len(states) - 1
    J = len(sq) + 1
    path = 'e'
    while (I != 0) and (J != 0):
        cell = P[I][J]
        path = path + states[cell]
        J = J - 1
        I = cell
    return path[::-1]


if __name__ == '__main__':
    # Initial input
    seq = 'ATCGCGTGGT'
    States = ['b', 'Y', 'N', 'e']
    transition_p = [[0, 0.2, 0.8, 0],
                    [0, 0.7, 0.2, 0.1],
                    [0, 0.1, 0.8, 0.1],
                    [0, 0, 0, 0]]
    emission_p = [[0, 0, 0, 0],
                  [0.1, 0.4, 0.4, 0.1],
                  [0.25, 0.25, 0.25, 0.25],
                  [0, 0, 0, 0]]
    H_emission_i = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    # Compute the Viterbi and pointer matrices
    results = Viterbi(seq, States, transition_p, emission_p, H_emission_i)
    V = results[0]
    Ptr = results[1]
    Preatty_Matrix(V)
    Preatty_Matrix(Ptr)
    Viterbi_path = Traceback(States, Ptr, seq)
    print("the Viterbi path for the sequence %s\n is %s\n with a probability of %r" % (
    seq, Viterbi_path, '{:.2e}'.format(V[len(States) - 1][len(seq) + 1])))
