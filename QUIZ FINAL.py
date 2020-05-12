#welcome screen
def introduction():
  for i in range(0,44):print("*",end="*")
  print("\n..................................WELCOME TO THE QUIZ...............................")
  print("\n***************************** INSTRUCTIONS TO PLAY THE GAME*************************")
  print("\n 1) enter your name ")
  print("\n 2) enter the subject number you want to attempt (1,2,3,4 or 5) .")
  print("\n 3) your quiz will began and now play the game.")
  print("\n 4) total 10 questions will be displayed(one by one) along with there four options ")
  print("\n 5) you have to choose any one option among the four given options")
  print("\n 6) at the last you will be rewarded marks according to your correct answers")
def welcome():
  for i in range(0,37):print("*",end="*")
  print("\n..................................WELCOME TO THE QUIZ...............................")
  pname=input("enter your name : ")
  print(" choose any one subject (1 or 2 or 3 or 4 or 5) :")
  print(" 1)General  Knowledge ")
  print(" 2)Computer ")
  print(" 3)Geography ")
  print(" 4)History ")
  print(" 5)English ")
  ch=input()
  if ch=='1':
    GK()
  elif ch=='2':
    Computer()
  elif ch=='3':
    Geography()
  elif ch=='4':
      History()
  elif ch=='5':
      English()
  else:
    print(pname,"good bye , Have a nice day ")
    exit(0)
  for i in range(0,37):print("*",end="*")
  print("\n")

def GK():
  q=[]
  q.append("Q1) The Plaka is the oldest quarter of which city?")
  
  
  q.append("Q2) What is an axolotl?")
  

  q.append("Q3) The Panama Canal was officially opened by which US president?")
  
  
  q.append("Q4) In which opera did Maria Callas make her last appearance at Covent Garden?")
  
  
  q.append("Q5) After Adam, Eve, Cain and Abel who is the next person mentioned in the Bible?")
  
  
  q.append("Q6) India is a federal union comprising twenty-nine states and how many union territories?")
  
  
  q.append("Q7) Which of the following is the capital of Arunachal Pradesh?")
  
  
  q.append("Q8) What are the major languages spoken in Andhra Pradesh?")
  
  
  q.append("Q9) What is the state flower of Haryana?")
  
  
  q.append("Q10)Which of the following states is not located in the North?")
  
  


  opta=[]
  opta.append("a) Athens")
  opta.append("a) A nerve in the brain")
  opta.append("a) Calvin Coolidge ")
  opta.append("a) Carmen ")
  opta.append("a) Enoch ")
  opta.append("a) 6")
  opta.append("a) Itanagar")
  opta.append("a) English and Telugu")
  opta.append("a) Lotus")
  opta.append("a) Jharkhand")
  

  optb=[]
  optb.append("b) Prague")
  optb.append("b) A multi-axled vehicle")
  optb.append("b) Herbert Hoover")
  optb.append("b) Tosca")
  optb.append("b) Jubal")
  optb.append("b) 7")
  optb.append("b) Dispur")
  optb.append("b) Telugu and Urdu")
  optb.append("b) Rhododendron")
  optb.append("b) Jammu and Kashmir")
  

  optc=[]
  optc.append("c) Rome")
  optc.append("c) A type  of  mortice  lock")
  optc.append("c) Theodore Roosevelt")
  optc.append("c) Madame Butterfly")
  optc.append("c) Lamech")
  optc.append("c) 8")
  optc.append("c) Imphal")
  optc.append("c) Telugu and Kannada")
  optc.append("c) Golden Shower")
  optc.append("c) Himachal Pradesh")
  

  optd=[]
  optd.append("d) Vienna \n")
  optd.append("d) A species of salamander \n")
  optd.append("d) Woodrow Wilson \n")
  optd.append("d) La Boheme \n")
  optd.append("d) Zillah \n")
  optd.append("d) 9 \n")
  optd.append("d) Panaji \n")
  optd.append("d) All of the above languages \n")
  optd.append("d) Not declared \n")
  optd.append("d) Haryana \n")
  

  keys=["a","d","d","b","a","b","a","b","a","a"]
  
  print("your questions are as follows : ")
  score=0
  for i in range(0,10):
    print(q[i])
    print(opta[i])
    print(optb[i])
    print(optc[i])
    print(optd[i])
    print("enter the correct option(a,b,c,d) : ")
    ans=input()
    if ans==keys[i]:
      score+=1
  print("yous score out of 10 is: ",score)

def Computer():
  q=[]
  q.append("Q1) A light sensitive decide that converts drawing, printed test or othr images in digital form is?")
  
  
  q.append("Q2) Which protocal provides e-mail facility among different hosts?")
  

  q.append("Q3) The basic architecture of computer was developed by?")
  
  
  q.append("Q4) In how many generations a computer can be classified?")
  
  
  q.append("Q5) Fifth generation computer are based on?")
  
  
  q.append("Q6) GUI stands for?")
  
  
  q.append("Q7) Time during which a job is processed by a computer?")
  
  
  q.append("Q8) The size of commanly used floppy disk?")
  
  
  q.append("Q9) Which one of the following is not the application software?")
  
  
  q.append("Q10)Which of the following circuit used as a memory device in computer?")


  opta=[]
  opta.append("a) Keyboard")
  opta.append("a) FTP")
  opta.append("a) John Von Neumann ")
  opta.append("a) 3 ")
  opta.append("a) Artificial Intelligence ")
  opta.append("a) Graph use interface")
  opta.append("a) Execution time")
  opta.append("a) 4.5")
  opta.append("a) Red Hat Linux")
  opta.append("a) Rectifiers")
  

  optb=[]
  optb.append("b) Clotter")
  optb.append("b) SMTP")
  optb.append("b) Charles Babbage")
  optb.append("b) 4")
  optb.append("b) Programming Intelligence")
  optb.append("b) Graphical universal interface")
  optb.append("b) Delay time")
  optb.append("b) 3.5")
  optb.append("b) MS Office")
  optb.append("b) Flip Flop")
  

  optc=[]
  optc.append("c) Scanner")
  optc.append("c) TELNET")
  optc.append("c) Blaise Pascal")
  optc.append("c) 5")
  optc.append("c) System Knowledge")
  optc.append("c) Graphical user interface")
  optc.append("c) Real time")
  optc.append("c) 3.25")
  optc.append("c) Open Office")
  optc.append("c) Comparators")
  

  optd=[]
  optd.append("d) OMR \n")
  optd.append("d) SNMP \n")
  optd.append("d) Garden Moore \n")
  optd.append("d) 6 \n")
  optd.append("d) None of these \n")
  optd.append("d) All of these \n")
  optd.append("d) Waiting time \n")
  optd.append("d) 5.5 \n")
  optd.append("d) Adobe pagemaker \n")
  optd.append("d) Attenuator \n")
  
  keys=["c","b","a","c","a","c","b","a","b","a"]
  
  print("your questions are as follows : ")
  score=0
  for i in range(0,10):
    print(q[i])
    print(opta[i])
    print(optb[i])
    print(optc[i])
    print(optd[i])
    print("enter the correct option(a,b,c,d) : ")
    ans=input()
    if ans==keys[i]:
      score+=1
  print("yous score out of 10 is: ",score)



def Geography():
  q=[]
  q.append("Q1) Study of the universe known as?")
  
  
  q.append("Q2) Approximately how many galaxies are there?")
  

  q.append("Q3) Big Bang Theory explains?")
  
  
  q.append("Q4) Big Bang was an explosion that occurs?")
  
  
  q.append("Q5) Which planet is known as dwarf planet  ?")
  
  
  q.append("Q6) Diameter of sun is?")
  
  
  q.append("Q7) Which are the main gases present in sun?")
  
  
  q.append("Q8) Surface temperature of sun is about?")
  
  
  q.append("Q9) Diameter of moon is?")

  
  q.append("Q10)Titan is satellite of?")


  opta=[]
  opta.append("a) Sociology")
  opta.append("a) 10 Billion")
  opta.append("a) Origin of Universe")
  opta.append("a) 10 billion years ago")
  opta.append("a) mercury")
  opta.append("a) 12 lakhs kms")
  opta.append("a) Hydrogen and Helium")
  opta.append("a) 5000 degree celcius")
  opta.append("a) 3375 km")
  opta.append("a) Mercury ")
  

  optb=[]
  optb.append("b) Cosmology")
  optb.append("b) 100 Billion")
  optb.append("b) Origin of sun")
  optb.append("b) 15 billion years ago")
  optb.append("b) pluto")
  optb.append("b) 13 lakhs kms")
  optb.append("b) Hydrogen and Argon")
  optb.append("b) 5005 degree celcius")
  optb.append("b) 3415 km")
  optb.append("b) Earth")
  

  optc=[]
  optc.append("c) Universology")
  optc.append("c) 1000 Billion")
  optc.append("c) Laws of physics")
  optc.append("c) 20 billion years ago")
  optc.append("c) mars")
  optc.append("c) 14 lakhs kms")
  optc.append("c) Argon and Helium")
  optc.append("c) 6000 degree celcius")
  optc.append("c) 3425 km")
  optc.append("c) Venus")
  

  optd=[]
  optd.append("d) Petology \n")
  optd.append("d) 10000 Billion \n")
  optd.append("d) None of the above \n")
  optd.append("d) 25 billion years ago \n")
  optd.append("d) uranus \n")
  optd.append("d) 15 lakhs kms \n")
  optd.append("d) Hydrogen and Carbon Diaoxide \n")
  optd.append("d) 6005 degree celcius \n")
  optd.append("d) 3475 km \n")
  optd.append("d) Saturn \n")
  
  keys=["b","b","a","b","b","c","a","b","d","d"]
  
  print("your questions are as follows : ")
  score=0
  for i in range(0,10):
    print(q[i])
    print(opta[i])
    print(optb[i])
    print(optc[i])
    print(optd[i])
    print("enter the correct option(a,b,c,d) : ")
    ans=input()
    if ans==keys[i]:
      score+=1
  print("yous score out of 10 is: ",score)


def History():
  q=[]
  q.append("Q1) What was the time period of Indus Civilization/Harappan Civilization?")
  
  
  q.append("Q2) Which was the largest site of Indus Civilization?")
  

  q.append("Q3) Which is the largest indin site of Indus Civilization?")
  
  
  q.append("Q4) Which two indus sites found in Afghanistan?")
  
  
  q.append("Q5) Which was the ancient port of Indus Civilization?")
  
  
  q.append("Q6) Which is the oldest text in the world?")
  
  
  q.append("Q7) How many Mandalas Rig Veda contains?")
  
  
  q.append("Q8) Which veda is important for Indian Music?")
  
  
  q.append("Q9) Ajatasatru was son of?")
  
  
  q.append("Q10)The Shisunaga Dynasty was overthrown by?")


  opta=[]
  opta.append("a) 2400BC-1700BC")
  opta.append("a) Mohenjodaro")
  opta.append("a) Mohenjodaro")
  opta.append("a) Lothal and Daimabad")
  opta.append("a) Harappa")
  opta.append("a) Yajur Veda")
  opta.append("a) 9 Mandalas")
  opta.append("a) Sama Veda")
  opta.append("a) Bimisara")
  opta.append("a) Bimisara")
  

  optb=[]
  optb.append("b) 2400BC-1750BC")
  optb.append("b) Lothal")
  optb.append("b) Lothal")
  optb.append("b) Shatughai and Dainabad")
  optb.append("b) Lothal")
  optb.append("b) Atharva Veda")
  optb.append("b) 10 Mandalas")
  optb.append("b) Yajur Veda")
  optb.append("b) Udayin")
  optb.append("b) Ajatashatru")
  

  optc=[]
  optc.append("c) 2500BC-1700BC")
  optc.append("c) Chanhudaro")
  optc.append("c) Chanhudaro")
  optc.append("c) Shatughai and Dainabad")
  optc.append("c) Dholavira")
  optc.append("c) Rig Veda")
  optc.append("c) 11 Mandalas")
  optc.append("c) Atharva Veda")
  optc.append("c) Shisunaga")
  optc.append("c) Mahapadma")
  

  optd=[]
  optd.append("d) 2500BC-1750BC \n")
  optd.append("d) Dholavira \n")
  optd.append("d) Dholavira \n")
  optd.append("d) Mundigaq and Dainabad \n")
  optd.append("d) Surkotada \n")
  optd.append("d) Sama Veda \n")
  optd.append("d) 12 Mandalas \n")
  optd.append("d) Rig Veda \n")
  optd.append("d) None of these \n")
  optd.append("d) Chandragupta Maurya \n")
  
  keys=["d","a","d","c","b","c","b","a","a","c"]
  
  print("your questions are as follows : ")
  score=0
  for i in range(0,10):
    print(q[i])
    print(opta[i])
    print(optb[i])
    print(optc[i])
    print(optd[i])
    print("enter the correct option(a,b,c,d) : ")
    ans=input()
    if ans==keys[i]:
      score+=1
  print("yous score out of 10 is: ",score)



def English():
  q=[]
  q.append("Q1) Extreme old age when a man behaves like a fool?")
  
  
  q.append("Q2) That which cannot be corrected?")
  

  q.append("Q3) The study of ancient society?")
  
  
  q.append("Q4) A person of good understanding knowledge and resoning power?")
  
  
  q.append("Q5) A person who insists on something?")
  
  
  q.append("Q6) State in which the few govern the many?")
  
  
  q.append("Q7) List of the business or subjects to be considered at a meeting?")
  
  
  q.append("Q8) Leave or remove from a place considered dangerous?")
  
  
  q.append("Q9) A person pretending to be somebody he is not?")

  
  q.append("Q10)A person who knows many foreign languages?")


  opta=[]
  opta.append("a) Imbecility")
  opta.append("a) Unintelligible")
  opta.append("a) Anthropology")
  opta.append("a) Expert")
  opta.append("a) Disciplinarian")
  opta.append("a) Monarchy")
  opta.append("a) Schedule")
  opta.append("a) Evacuate")
  opta.append("a) Magician")
  opta.append("a) Linguist")
  

  optb=[]
  optb.append("b) Youth")
  optb.append("b) Indelible")
  optb.append("b) Archaeology")
  optb.append("b) Intellectual")
  optb.append("b) Stickler")
  optb.append("b) Oligarchy")
  optb.append("b) Timetable")
  optb.append("b) Evade")
  optb.append("b) Rogue")
  optb.append("b) Grammarian")
  

  optc=[]
  optc.append("c) Dotage")
  optc.append("c) Illegible")
  optc.append("c) History")
  optc.append("c) Snob")
  optc.append("c) Instantaneous")
  optc.append("c) Plutocracy")
  optc.append("c) Agenda")
  optc.append("c) Avoid")
  optc.append("c) Liar")
  optc.append("c) Polyglot")
  

  optd=[]
  optd.append("d) Superannuation \n")
  optd.append("d) Incorrigible \n")
  optd.append("d) Ethnology \n")
  optd.append("d) Literate \n")
  optd.append("d) Boaster \n")
  optd.append("d) Autocracy \n")
  optd.append("d) Plan \n")
  optd.append("d) Exterminate \n")
  optd.append("d) Impostor \n")
  optd.append("d) Bilingual \n")
  
  keys=["c","d","b","b","b","b","c","a","d","a"]
  
  print("your questions are as follows : ")
  score=0
  for i in range(0,10):
    print(q[i])
    print(opta[i])
    print(optb[i])
    print(optc[i])
    print(optd[i])
    print("enter the correct option(a,b,c,d) : ")
    ans=input()
    if ans==keys[i]:
      score+=1
  print("yous score out of 10 is: ",score)

def main():
  introduction()
  def cls():
    print('\n'*6)
  cls()  
  welcome()
  print("\n Do you want to continue 'Y' or 'N'? \n")
  print("Enter your choice ")
  c=input()
  if c=='Y' or c=='y':
      welcome()
  else:
      print("THANK YOU FOR PLAYING THE GAME ")
      exit(0)
  print("\n"*15)
  

if __name__=="__main__":
  main()
  


      
    

    
    



















 
