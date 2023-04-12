import random;

response = input('pressione y:')

def dados(response):
  while response == "y":
    no = random.randint(1,6)  
    if no == 1 :
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print(input('pressione y para jogar de novo e n para sair:'))
    if no == 2 :
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[-----]")
        print(input('pressione y para jogar de novo e n para sair:'))
    if no == 3 :
        print("[-----]")
        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print("[-----]")
        print(input('pressione y para jogar de novo e n para sair:'))
    if no == 4 :
        print("[-----]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[-----]")
        print(input('pressione y para jogar de novo e n para sair:'))
    if no == 5 :
        print("[-----]")
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[ 0 0 ]")
        print("[-----]")
        print(input('pressione y para jogar de novo e n para sair:'))
    if no == 6 :
        print("[-----]")
        print("[ 000 ]")
        print("[     ]")
        print("[ 000 ]")
        print("[-----]") 
        print(input('pressione y para jogar de novo e n para sair:'))

dados(response)        
