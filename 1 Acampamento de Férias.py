
temp = []


while True:
    c = int(input())
    if c == 0:
        break
      
    else:
        for n in range(0,c):
            # pega a lista e a transforma numa nova lista com a operação str
            nome, num = map(str, input().split())
            num = int(num)
            temp.append([nome,num])
        
        
        
    inicio = temp[0][1]
    inicio_ant = 0
    aux = 0
    auy = len(temp)
        
    for j in range(1,c):
        if inicio%2==0:
            if j==1:
                y = auy
            else:
                if inicio_ant%2!=0:
                    y = aux+1
                else:
                    y = auy
            for i in range(inicio, 0, -1):
                if y==0:
                    y = len(temp)-1
                else:
                    y-=1
              
            eliminado = temp.pop(y)
            auy = y
            inicio_ant = inicio
        else:
            if j==1:
                x = aux
            else:
                if inicio_ant%2!=0:
                    x = aux
                else:
                    x = auy-1
            for i in range(1, inicio+1):
                x+=1
                if x==len(temp):
                    x = 0
            
            eliminado = temp.pop(x)
            aux = x-1
            inicio_ant = inicio
            
        inicio = eliminado[1]
        
        
    print("Vencedor(a):",temp[0][0])
    temp.pop(0)
 
