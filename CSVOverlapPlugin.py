import numpy

class CSVOverlapPlugin:
   def input(self, inputfile):
      filestuff = open(inputfile, 'r')
      self.parameters = dict()
      for line in filestuff:
         contents = line.strip().split('\t')
         self.parameters[contents[0]] = contents[1]
      
      firstfile = open(self.parameters["csvfile1"], 'r')
      firstline = firstfile.readline()
      self.bacteria1 = firstline.strip().split(',')
      if (self.bacteria1.count('\"\"') != 0):
         self.bacteria1.remove('\"\"')
      self.n1 = len(self.bacteria1)
      self.m = 0
      self.ADJ1 = []
      for line in firstfile:
            self.ADJ1.append([])
            contents = line.strip().split(',')
            for j in range(self.n1):
               value = float(contents[j+1])
               self.ADJ1[self.m].append(value)
            self.m += 1

      secondfile = open(self.parameters["csvfile2"], 'r')
      firstline = secondfile.readline()
      self.bacteria2 = firstline.strip().split(',')
      if (self.bacteria2.count('\"\"') != 0):
         self.bacteria2.remove('\"\"')
      self.n2 = len(self.bacteria2)
      self.ADJ2 = numpy.zeros([self.m, self.n2])
      i = 0
      for line in secondfile:
            contents = line.strip().split(',')
            for j in range(self.n2):
               value = float(contents[j+1])
               self.ADJ2[i][j] = value
            i += 1

      
   def run(self):
      #print(self.bacteria2)
      self.vectors = dict()
      self.errors = dict()
      for j in range(len(self.bacteria1)):
         if self.bacteria1[j] in self.bacteria2:
            # If in both, add vectors to comparison
            self.vectors[self.bacteria1[j]] = (numpy.ndarray(self.m), numpy.ndarray(self.m))
            k = self.bacteria2.index(self.bacteria1[j]) 
            for i in range(self.m):
               self.vectors[self.bacteria1[j]][0][i] = self.ADJ1[i][j]
               self.vectors[self.bacteria1[j]][1][i] = self.ADJ2[i][k]
            A = self.vectors[self.bacteria1[j]][0]
            B = self.vectors[self.bacteria1[j]][1]
            if ((numpy.linalg.norm(A) * numpy.linalg.norm(B)) != 0):
               self.errors[self.bacteria1[j]] = (A.dot(B)) / (numpy.linalg.norm(A) * numpy.linalg.norm(B))
            else:
               self.errors[self.bacteria1[j]] = 0
   
   def output(self, outputfile):
      filestuff = open(outputfile, 'w')
      filestuff.write("\"\",\"Overlap\"\n")
      for key in self.errors:
         filestuff.write(key+","+str(self.errors[key])+"\n")
