from datetime import datetime, date, timedelta
producto={"123":["aceite",10,float(50.5),int(0),date(2018,7,10),"a",""],
          "1234":["papas",10,float(60),int(3),date(2018,8,10),"v",""],
          "12345":["naranjas",10,float(60),int(4),date(2018,6,9),"v",""],
          "123456":["leche",10,float(50),int(2),date(2018,6,12),"l",""]}
# menu
menu=""
while menu != "9":
    print("1-INGRRESAR MONTO REQUERIDO DE STOCK DEL PRODUCTO:")
    print("2-REALIZAR COMPRA:")
    print("3-AGREGAR PRODUCTO:")
    print("31-ACTUALIZAR PRECIO DE PRODUCTO")
    print("4-ELIMINAR PRODUCTO:")
    print("5-DATOS DE CLIENTE PARA ENVIOS A DOMICILIO:")
    print("6-INFORMACION SOBRE LA SECCION MAS VENDIDA:")
    print("7-ARTICULO MAS VENDIDO:")
    print("8-LISTA DE PRODUCTOS")
    print("9-SALIR DEL PROGRAMA:")
    menu=input()

    if menu == "1":
        # reponer stock
        print("INGRESAR STOCK MINIMO REQUERIDO:")
        stockrequerido=int(input())
        
    # fecha
    from datetime import datetime, date, timedelta
    fecha=datetime.now().date()
    productovencido={}
    claveg=[]

    for clave in producto.keys():
        fechad=producto[clave][4]

        if fechad < fecha:
            t=producto[clave][0]
            s=producto[clave][1]
            p=producto[clave][2]
            c=producto[clave][3]
            f=producto[clave][4]
            se=producto[clave][5]
            productovencido[clave]=[t,s,p,c,f,se]
            claveg=claveg+[clave]
            
    for pos in claveg:
        del producto[pos]

    if menu == "2":
        #para comprar, traer el precio,actualizar stock cuando se vende, si vence en 1 semana que avise en el producto
        articulomayorventa=0
        total=0
        unidad=[]
        descripcion=[]
        seccion=[]
        preciot=[]
        ticket={}
        totalcompra=0
        miclave=""
        volver=""
        while volver != "exit":
            print("INGRESAR terminar CUANDO DESEA IMPRIMIR EL TICKET:")
            miclave=""
            while miclave  != "terminar":
                print("INGRESAR CODIGO DE PRODUCTO:")
                miclave=input()
                for clave in producto.keys():
                    dias=timedelta(days=7)
                    fechap=producto[clave][4]
                    fechadesc= fecha + dias 
                    if fechadesc == fechap :
                        producto[clave][6]="si desc"
                    else:
                        producto[clave][6]="no desc"                    

                    if clave== miclave:
                        print("Producto existente:"" "+ producto[clave][0])
                        print("INGRESAR CANTIDAD DE " " " +producto[miclave][0]+":")
                        cantidad=int(input())
                        if cantidad <= producto[clave][1]:
                            
                            
                            producto[clave][3]=producto[clave][3]+ cantidad
                            stockactualizado= producto[clave][1]-cantidad
                            producto[clave][1]=stockactualizado
                            if producto[clave][1] < stockrequerido:
                                producto[clave][1]=stockrequerido
                            if producto[clave][6] == "si desc":
                                precio= producto[clave][2] * 0.9
                            else:
                                precio=producto[clave][2]
                            total= total + (cantidad * precio)
                            unidad=cantidad
                            descripcion= producto[clave][0]
                            seccion=producto[clave][5]
                            preciot=precio * cantidad
                            totalcompra=totalcompra +preciot
                            ticket[clave]=[descripcion,unidad,preciot,seccion]
                        else:
                            print("No hay stock suficiente quedan solo:" " "+ str(producto[clave][1])+ " ""unidades") 

                    else:
                        igual=0
                        for clave in producto.keys():
                            if miclave== clave or miclave =="terminar":
                                igual=+ 1
                if igual == 0:
                    print("El producto no existe") 
                            
            print("DESCRIP","  UNI","PREC"," SEC",)
            for clave in ticket.keys():
                print(ticket[clave])
            print("PRECIO TOTAL:"" " + str(totalcompra))
            
            print("SI QUIERE VOLVER AL MENU PRINCIPAL INGRESE exit, SI QUIERE REALIZAR OTRA COMPRA INGRESE continuar:")
            volver=input()
        
    if menu == "6":
        # determinar el producto mas vendido dependiendo del tipo
        salir=""
        totalv=0
        totall=0
        totalc=0
        totala=0
        for clave in producto.keys():
            if producto[clave][5]=="v":
                totalv = totalv + producto[clave][3]
            if producto[clave][5]=="l":
                totall = totall + producto[clave][3]
            if producto[clave][5]=="c":
                totalc = totalc + producto[clave][3]
            if producto[clave][5]=="a":
                totala = totala + producto[clave][3]
                    
        if totalv>totall and totalv>totalc and totalv>totala:
            print("SE VENDIO MAS EN EL AREA DE VERDULERIA")
        elif totall>totalv and totall>totalc and totall>totala:
            print("SE VENDIO MAS EN EL AREA DE LACTEOS")
        elif totalc>totalv and totalc>totall and totalc>totala:
            print("SE VENDIO MAS EN EL AREA DE CARNICERIA")
        elif totala> totalv and totala>totall and totala>totalc:
            print("SE VENDIO MAS EN EL AREA ALMACEN")
        print("INGRESAR exit PARA VOLVER AL MENU:")
        salir=input()
        
    if menu == "7":
        articulomayorventa=0
        # determinar cual es el articulo mas vendido
        salir=""
        for clave in producto.keys():
            if articulomayorventa < producto[clave][3]:
                articulomayorventa=producto[clave][3]
                nombrearticulo=producto[clave][0]
                
        print("ARTICULO MAS VENDIDO ES:"  " " + nombrearticulo )
        print("INGRESAR exit PARA VOLVER AL MENU:")
        salir=input()
    
    if menu == "5":
        # pedir datos de cliente para envios a domicilio
        salir=""
        while salir !="exit":
            datos={}
            print("INGRESAR NOMBRE:")
            nombred=input()
            datos["nombre"]=nombred
            print("TELEFONO:")
            telefonod=input()
            datos["telefono"]=telefonod
            print("INGRESAR CALLE:")
            called=input()
            datos["calle"]=called
            print("ALTURA:")
            alturad=input()
            datos["altura"]=alturad
            print("PISO Y DEPTO:")
            pisodeptod=input()
            datos["pisodepto"]=pisodeptod
            print(datos)
            print("INGRESE exit PARA VOLVER AL MENU:")
            salir=input()
        
    if menu == "3":
        #agregar producto mas sus datos
        salir=""    
        while salir !="exit":
            print("INGRESAR CODIGO:")
            codigo= input()
            print("INGRESAR TIPO:")
            tipo=input()
            print("INGRESAR STOCK:")
            stock=input()
            print("INGRESAR PRECIO:")
            precio=int(input())
            cant=int(0)
            print("INGRESAR FECHA CON FORMATO Y-m-d:")
            print("Y:")
            y=input()
            print("M:")
            m=input()
            print("D:")
            d=input()
            fechai=date(int(y),int(m),int(d))
            print("INGRESAR CON UNA LETRA A QUE SECCION CORRESPONDE:")
            print("VERDULERIA: v LACTEOS: l CARNICERIA: c ALMACEN: a")
            seccion=input()
            t=0
            for clave in producto.keys():
                if clave == codigo:
                    t=1
            if t == 0:
                producto[codigo]=[tipo,stock,precio,cant,fechai,seccion]
                
            else:
                print("El codigo ya existe")
            print("INGRESE exit PARA VOLVER AL MENU O continuar PARA AGREGAR PRODUCTO:")
            salir=input("")
            
    if menu == "31":
        # actualizar precio de producto
        bye=""
        while bye !="exit":
            print("INGRESAR CODIGO PARA ACTUALIZAR PRECIO")
            codigo=input()
            s=0
            preciou=0
            aumento=0
            for clave in producto.keys():
                if clave == codigo:
                    s=1
            if s == 0:
                print("El codigo no se encuentra")
            else:
                print("INGRESAR PORCENTAJE DE AUMENTO")
                porcentaje=int(input())
                preciou=producto[codigo][2]
                aumento= (preciou * porcentaje)/100
                preciou=preciou + aumento
                producto[codigo][2]= preciou
            print("INGRESE exit PARA VOLVER AL MENU O continuar PARA BORRAR PRODUCTO:")
            bye=input()
            
    if menu == "4":
        # borrar producto
        bye=""
        while bye !="exit":
            print("INGRESAR CODIGO A BORRAR:")
            codigo=input()
            s=0
            for clave in producto.keys():
                if clave == codigo:
                    s=1
            if s ==0:
                print("El codigo no se encuentra")
            else:
                del producto[codigo]
                print(producto)
            print("INGRESE exit PARA VOLVER AL MENU O continuar PARA BORRAR PRODUCTO:")
            bye=input()
            
    if menu == "8":
        # listar productos
        salir=""
        for key in producto:
          print( key, ":", producto[key])
        print("INGRESAR exit PARA VOLVER AL MENU:")
        salir=input()

