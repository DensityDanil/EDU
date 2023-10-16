def sentense_to_num_sequence(sentense):
    data = sentense.split(' ')

    out = []
    ascii_en_const = 96
    exceptions = list(".,;-:'!?(){}")
    #print(exceptions)
    for word in data:
        #num_seq = ''.join([f"*{str(ord(char)-97)}*"
        #                   if len(str(ord(char)-ascii_en_const))==2
        #                   else f".{str(ord(char)-ascii_en_const)}."
        #                   for char in word.lower()])

        num_seq = [ord(char)-96 for char in word.lower() if char not in exceptions]
         
        out.append(num_seq)

    data = [''.join([g.lower() for g in k if g not in exceptions]) for k in data ]
    translate = '\n'.join(list(set([f"{w}\t{sum(c)}\t{','.join(list(map(str,ss))) }" for w,c,ss in zip(data,out,out)  ] )))
    
    out = '\n'.join(translate)
    print(translate)

    
    return out
    
test1='''For classes having irreparable combat losses and at least three ships in the database, display the name of the class and the number of ships sunk. end'''
test1='''separate part of this book. Here, we introduce these parts in reverse order because by starting from the end you can better understand the reason for the beginning.
COMPLEXITY THEORY
Computer problems come in different varieties; some are easy, and some are hard. For example, the sorting problem is an easy one. Say that you need to arrange a list of numbers in ascending order. Even a small computer can sort a million numbers rather quickly. Compare that to a scheduling problem. Say that you must ﬁnd a schedule of classes for the entire university to satisfy some reasonable constraints, such as that no two classes take place in the same room at the same time. The scheduling problem seems to be much harder than the sorting problem. If you have just a thousand classes, ﬁnding the best schedule may require centuries, even with a supercomputer.
What makes some problems computationally hard and others easy?
This is the central question of complexity theory. Remarkably, we don’t know the answer to it, though it has been intensively researched for over 40 years. Later, we explore this fascinating question and some of its ramiﬁcations. In one important achievement of complexity theory thus far, researchers have discovered an elegant scheme for classifying problems according to their computational difﬁculty. It is analogous to the periodic table for classifying elements according to their chemical properties. Using this scheme, we can demonstrate a method for giving evidence that certain problems are computationally hard, even if we are unable to prove that they are. You have several options when you confront a problem that appears to be computationally hard. First, by understanding which aspect of the problem is at the root of the difﬁculty, you may be able to alter it so that the problem is more easily solvable. Second, you may be able to settle for less than a perfect solution to the problem. In certain cases, ﬁnding solutions that only approximate the perfect one is relatively easy. Third, some problems are hard only in the worst case situation,buteasy mostof the time. Depending on the application,you may be satisﬁed with a procedure that occasionally is slow but usually runs quickly. Finally, you may consider alternative types of computation, such as randomized computation, that can speed up certain tasks. One applied area that has been affected directly by complexity theory is the ancient ﬁeld of cryptography. In most ﬁelds, an easy computational problem is preferable to a hard one because easy ones are cheaper to solve. Cryptography is unusual because it speciﬁcally requires computational problems that are hard, rather than easy. Secret codes should be hard to break without the secret key or password. Complexity theory has pointed cryptographers in the direction of computationally hard problems around which they have designed revolutionary new codes.'''
test1='''Alphabet A finite, nonempty set of objects called symbols Argument An input to a function Binary relation A relation whose domain is a set of pairs Boolean operation An operation on Boolean values Boolean value The values TRUE or FALSE, often represented by 1 or 0 Cartesian product An operation on sets forming a set of all tuples of elements from respective sets Complement An operation on a set, forming the set of all elements not present Concatenation An operation that joins strings together Conjunction Boolean AND operation Connected graph A graph with paths connecting every two nodes Cycle A path that starts and ends in the same node Directed graph A collection of pointsand arrows connectingsome pairs of points Disjunction Boolean OR operation Domain The set of possible inputs to a function Edge A line in a graph Element An object in a set Empty set The set with no members Empty string The string of length zero Equivalence relation A binary relation that is reﬂexive, symmetric, and transitive Function An operation that translates inputs into outputs Graph A collection of points and lines connecting some pairs of points Intersection An operation on sets forming the set of common elements k-tuple A list of k objects Language A set of strings Member An object in a set Node A point in a graph Ordered pair A list of two elements Path A sequence of nodes in a graph connected by edges Predicate A function whose range is {TRUE, FALSE} Property A predicate Range The set from which outputs of a function are drawn Relation A predicate, most typically when the domain is a set of k-tuples Sequence A list of objects Set A group of objects Simple path A path without repetition Singleton set A set with one member String A finite list of symbols from an alphabet Symbol A member of an alphabet Tree A connected graph without simple cycles Union An operation on sets combining all elements into a single set Unordered pair A set with two members Vertex A point in a graph
'''
r = sentense_to_num_sequence(test1)
##For -> 39 -> 6,15,18
##classes -> 78 -> 3,12,1,19,19,5,19
##having -> 61 -> 8,1,22,9,14,7
##irreparable -> 105 -> 9,18,18,5,16,1,18,1,2,12,5
##combat -> 54 -> 3,15,13,2,1,20
##losses -> 89 -> 12,15,19,19,5,19
##and -> 19 -> 1,14,4
##at -> 21 -> 1,20
##least -> 57 -> 12,5,1,19,20
##three -> 56 -> 20,8,18,5,5
##ships -> 71 -> 19,8,9,16,19
##in -> 23 -> 9,14
##the -> 33 -> 20,8,5
##database, -> 1 -> 4,1,20,1,2,1,19,5,-52
##display -> 86 -> 4,9,19,16,12,1,25
##the -> 33 -> 20,8,5
##name -> 33 -> 14,1,13,5
##of -> 21 -> 15,6
##the -> 33 -> 20,8,5
##class -> 54 -> 3,12,1,19,19
##and -> 19 -> 1,14,4
##the -> 33 -> 20,8,5
##number -> 73 -> 14,21,13,2,5,18
##of -> 21 -> 15,6
##ships -> 71 -> 19,8,9,16,19
##sunk. -> 15 -> 19,21,14,11,-50
##end -> 23 -> 5,14,4
