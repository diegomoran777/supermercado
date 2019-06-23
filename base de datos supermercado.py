import sqlite3

conn = sqlite3.connect("supermercado.db")
print("opened database succefully")

#crear tabla
#conn.execute('''create table productos
 #            (codigo varchar(50),
 #             nombre varchar(50),
 #             stock  integer,
 #             precio integer,
 #             fecha date format YYYY-MM-DD ,
 #             seccion varchar(1),
 #             descuento varchar(50));''')
#print("tabla creada exitosamente")
#ingresar datos
#conn.execute("insert into productos (codigo,nombre,stock,precio,fecha,seccion,descuento) values ('1234','papas',10,60,('2018-8-10'),'a','')")
#conn.execute("insert into productos (codigo,nombre,stock,precio,fecha,seccion,descuento) values ('1235','naranjas',10,60,('2018-6-9'),'v','')")
#conn.commit()
                 
#comienza el programa    
from datetime import datetime, date, timedelta

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
    fecha2=conn.execute("select * from productos")
    conn.commit()

    for fila in fecha2:
        f=fila[4]
        f2=f.split("-")
        y=int(f2[0])
        m=int(f2[1])
        d=int(f2[2])
        fechad=date(y,m,d) 
        
        if  fechad < fecha:
            cod=fila[0]
            nom=fila[1]
            stoc=fila[2]
            prec=fila[3]
            fech=fila[4]
            sec=fila[5]
            desc=fila[6]
            cant_vendida=fila[7]
            productovencido[cod]=[nom,stoc,prec,fech,sec,desc,cant_vendida]
            codborrar=fila[0]
            conn.execute("DELETE FROM productos WHERE codigo=" + codborrar)
            conn.commit()
            
                       
    if menu == "2":
        #para comprar, traer el precio,actualizar stock cuando se vende, si vence en 1 semana que avise en el producto
        articulomayorventa=0
        total=0
        unidad=[]
        descripcion=[]
        seccion=[]
        preciot=[]
        ticket={}
        desc=" si desc"
        nodesc="no desc"
        totalcompra=0
        miclave=""
        volver=""
        while volver != "exit":
            print("INGRESAR terminar CUANDO DESEA IMPRIMIR EL TICKET:")
            miclave=""
            while miclave  != "terminar":
                print("INGRESAR CODIGO DE PRODUCTO:")
                miclave=input()
                db=conn.execute("select * from productos")
                conn.commit()
                
                for fila in db :
                    dias=timedelta(days=7)
                    fechadesc=fecha + dias
                    codigo=fila[0]
                    f=fila[4]
                    f2=f.split("-")
                    y=int(f2[0])
                    m=int(f2[1])
                    d=int(f2[2])
                    fechap=date(y,m,d)
                    
                    if fechadesc == fechap :
                        conn.execute("UPDATE productos set descuento ='" + desc + "'where codigo='" + codigo +"'")
                        conn.commit()
                    else:
                        conn.execute("UPDATE productos set descuento ='" + nodesc + "'where codigo='" + codigo +"'")
                        conn.commit()                    

                    if codigo == miclave:
                        print("Producto existente:"" "+ fila[1])
                        print("INGRESAR CANTIDAD DE " " " + fila[1]+":")
                        cantidad=int(input())
                        stoc=fila[2]
                        cant=fila[7]
                        if cantidad <= stoc : 
                            cant=cant + cantidad
                            stockactualizado= stoc-cantidad
                            sa=str(stockactualizado)
                            ca=str(cant)
                            conn.execute("UPDATE productos set stock ='" + sa + "'where codigo='" + codigo +"'")
                            conn.commit()    
                            conn.execute("UPDATE productos set cant_vendida ='" + ca + "'where codigo='" + codigo +"'")
                            conn.commit()
                            if stockactualizado < stockrequerido:
                                stoc=stockrequerido
                                st=str(stoc)
                                conn.execute("UPDATE productos set stock ='" + st + "'where codigo='" + codigo +"'")
                                conn.commit()
                            if fila[6] == "si desc":
                                precio= fila[3] * 0.9
                            else:
                                precio=fila[3]
                            total= total + (int(cantidad) * precio)
                            unidad=cantidad
                            descripcion= fila[1]
                            seccion=fila[5]
                            preciot=precio * cantidad
                            totalcompra=totalcompra +preciot
                            ticket[codigo]=[descripcion,unidad,preciot,seccion]
                        else:
                            print("No hay stock suficiente quedan solo:" " "+ str(stoc)+ " ""unidades") 
                            
                    else:
                        bd=conn.execute("select * from productos")
                        conn.commit()
                        igual=0
                        for fila in bd:
                            clave= fila[0]
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
        db=conn.execute("select * from productos")
        conn.commit()
        for fila in db:
            if fila[5]=="v":
                totalv = totalv + fila[7]
            if fila[5]=="l":
                totall = totall + fila[7]
            if fila[5]=="c":
                totalc = totalc + fila[7]
            if fila[5]=="a":
                totala = totala + fila[7]
                    
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
        db=conn.execute("select * from productos")
        conn.commit()
        salir=""
        for fila in db :
            if articulomayorventa < fila[7]:
                articulomayorventa=fila[7]
                nombrearticulo=fila[1]
                
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
            codigo= input("")
            print("INGRESAR NOMBRE:")
            nombre=input("")
            print("INGRESAR STOCK:")
            stock=input("")
            print("INGRESAR PRECIO:")
            precio=input("")
            print("INGRESAR FECHA CON FORMATO Y-m-d:")
            fecha=input("")
            print("INGRESAR CON UNA LETRA A QUE SECCION CORRESPONDE:")
            print("VERDULERIA: v LACTEOS: l CARNICERIA: c ALMACEN: a")
            seccion=input("")
            bd=conn.execute("select * from productos")
            conn.commit()
            t=0
            for fila in bd:
                clave=fila[0]
                if clave == codigo:
                    t=1
            if t == 0:
                conn.execute("insert into productos (codigo,nombre,stock,precio,fecha,seccion,descuento,cant_vendida) values ('" + codigo + "', '"  + nombre + "', '" + stock + "', '" + precio + "','" + fecha + "','" + seccion + "','',0)")
                conn.commit()
            else:
                print("El codigo ya existe")
            print("INGRESE exit PARA VOLVER AL MENU O continuar PARA AGREGAR PRODUCTO:")
            salir=input("")
    if menu == "31":
        # actualizar precio de producto
        bye=""
        while bye !="exit":
            print("INGRESAR CODIGO PARA ACTUALIZAR PRECIO")
            codigo=input("")
            s=0
            preciou=0
            aumento=0
            db=conn.execute("select * from productos")
            conn.commit()
            for fila in db:
                clave=fila[0]
                if clave == codigo:
                    s=1
                    precio=fila[3]
            if s == 0:
                print("El codigo no se encuentra")
            else:
                print("INGRESAR PORCENTAJE DE AUMENTO")
                porcentaje=int(input())
                preciou= precio
                aumento= (preciou * porcentaje)/100
                preciou=preciou + aumento
                pc=str(preciou)
                conn.execute("UPDATE productos set precio='" + pc + "'where codigo='" + codigo +"'") 
            print("INGRESE exit PARA VOLVER AL MENU O continuar PARA BORRAR PRODUCTO:")
            bye=input()
            
    if menu == "4":
        # borrar producto
        bye=""
        while bye !="exit":
            print("INGRESAR CODIGO A BORRAR:")
            codigo=input("")
            db=conn.execute("select * from productos")
            conn.commit()
            s=0
            for fila in db:
                clave=fila[0]
                if clave == codigo:
                    s=1
            if s ==0:
                print("El codigo no se encuentra")
            else:
                conn.execute("delete from productos where codigo = " + codigo)
                conn.commit()
            print("INGRESE exit PARA VOLVER AL MENU O continuar PARA BORRAR PRODUCTO:")
            bye=input()
            
    if menu == "8":
        # listar productos
        db=conn.execute("select * from productos")
        conn.commit()
        salir=""
        for fila in db:
            print( fila)
        print("INGRESAR exit PARA VOLVER AL MENU:")
        salir=input()
