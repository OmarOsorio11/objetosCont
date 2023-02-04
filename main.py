# Version 2
import cv2
if __name__ == '__main__':
    #Leemos imagen a detectar contornos
    imagen = cv2.imread('pexels-img.jpg')

    #convertimos a escala de grises 
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    #Convertimos en imagen binaria
    _, th = cv2.threshold(grises, 220, 230, cv2.THRESH_BINARY)

    #Obtenemos los contornos
    cnts, _ = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #Fuente para escribir en imagen
    font= cv2.FONT_HERSHEY_SIMPLEX
    
    #Para cada contorno se encuenta su centro, se escribe el numero de contorno y se dibuja el contorno
    i=0
    for c in cnts:
        #Dibujamos el contorno
        cv2.drawContours(imagen, [c], 0, (255, 0, 0), 2)

        #Encontramos el centro de cada contorno
        M=cv2.moments(c)
        if(M["m00"]==0): M["m00"]=1
        x=int(M["m10"]/M["m00"])
        y = int(M["m01"]/M["m00"])
        mensaje='Num : ' + str(i+1)
        cv2.putText(imagen,mensaje,(x-30,y),font,0.4,(0,255,0),2,cv2.LINE_AA)
        
        #Mostramos imagen y esperamos a que el usuario presione siguiente
        cv2.imshow("Imagen",imagen)
        cv2.waitKey(0)
        i=i+1

    #Cerramos todas las ventanas     
    cv2.destroyAllWindows()
