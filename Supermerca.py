#-*- coding: utf-8 -*- 
# -*- coding: 850 -*-
import time
import os
import getpass
menur = True
prod_bodega = {}

def menucaja():
	# CONTENIDO DEL MENÚ CAJA (OPCION 2 DEL MENU PRINCIPAL)...............................
	print "======================================================================"
	print "==========    Se Encuentra en Caja Registradora             =========="     
	print "======================================================================"
	print " "
	print "A continuacion se le presenta dos opciones por favor elija la que desee:"
	time.sleep(2)
	print "Que desea Realizar?"
	print " "
	print "1. Comprar"
	print "2. Regresar al Menu Principal"
	print " "
	# INGRESO DE OPCIONES DENTRO DEL MENU CAJA............................................
	time.sleep(1)
	num_menur1 = raw_input("Ingrese Numero de Opcion: ")
	print " "
	# REDIRECCIONAMIENTOS ................................................................
	if num_menur1 == "1":
		os.system('cls')
		carrito()
	elif num_menur1 == "2":
		os.system('cls')
		menuprincipal()
	else:
		os.system('cls')
		print "Esta opcion no esta disponible porfavor vuelva a intentarlo"
		menucaja()
#****************************************************************************************
#******************************* Carrito de Compras *********************************
#****************************************************************************************
def carrito():
	# CONTENIDO DE LA OPCION COMPRAR (OPCION1 DEL MENU CAJA)..............................
	print " "
	print "======================================================================"
	print "========         Puede empezar a llenar su  CANASTA           ========"
	print "======================================================================"
	print ""
	subtotal = 0
	# VALIDACION DE PRODUCTOS EXISTENTES..................................................
	if len(prod_bodega)>0:
		value2=True
		while value2==True:
			# FOR PARA RECORRER EL DICCIONARIO E IMPRIMIR ELEMENTOS.......................
			for i in prod_bodega:
				print "Productos Disponibles: ", prod_bodega
				print " "
				nompro=raw_input("Producto a Llevar: ")
				print " "
				# VALIDACION DEL PRODUCTO SI EXISTE O NO..................................
				for elemento in prod_bodega:
					if proe_bodega[lemento][0]==nompro:
						cantidad=input("Cantidad Unitaria a comprar: ")
						print " "
						# ASIGNACION DE VARIABLES (CANTIDAD DE PRODUCTO POR PRECIO)
						sb=cantidad*prod_bodega[elemento][1]
						# ASIGNACION DE VARIABLES (CONTADOR MAS SB), VARIABLE GLOBAL
						subtotal = subtotal + sb
						print "*****%s Cant: %s Subtotal: Q.%s "%(elemento, cantidad,subtotal )
						print " "
						value3=True
						# ELECCION DE PRODUCTO NUEVAMENTE.................................
						while value3==True:
							seguir=raw_input("desea elegir otro articulo SI/NO: ")
							print " "
							if seguir.lower()=="si":
								os.system('cls')
								value2=True
								value3=False
							elif seguir.lower()=="no":
								value2 = False
								value3 = False
								print " "
								os.system('cls')
							else:
								print "opcion invalida"
								print " "
								value3=True
		else:
			factura(subtotal)
	else:
		print " "
		print "¿¡Qué!, ya se va?, no ha comprado nada aún, talvés es porque el Gerente no ha comprado productos para la tienda. "
		print " "

#****************************************************************************************
#********************************** Facturación *****************************************
#****************************************************************************************
def factura(compragen):
	value2=True
	cliente = raw_input("Nombre del Comprador: ")
	nit = raw_input("NIT: ")
	# CONTENIDO DE LA OPCION FACTURAR (OPCION 2 DEL MENU CAJA).............................
	print " "
	print "*. Gold"
	print "*. Silver"
	print "*. Presione cualquier tecla si no posee ninguna de las anteriores: "
	# VALIDACION PARA TARJETA CLIENTE......................................................
	while value2==True:
		tarcliente=raw_input("Posee tarjeta de Miembro? ¿Cuál?: ")
		print " "
		# TARJETA GOLD Y PROCEDIMIENTO....................................................
		if tarcliente.lower()=="gold":
			print "El Sr.(a): " + cliente +" posee tarjeta tipo: "+ tarcliente+ " por lo cual obtiene el 5%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			descuento = (compragen*0.05)
			totalcompra = compragen + iva - descuento
			print " "
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			print "__________________________"
			print " "
			efectivo = input("Cantidad de Pago en Efectivo: ")
			os.system('clear')
			print " "
			cambio = efectivo - compragen
			print "__________________________"
			print "__________________________"
			print " "
			print "NOMBRE: %s"%(cliente)
			print "NIT: %s"%(nit)
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
		# TARJETA SILVER Y PROCEDIMIENTO..................................................
		elif tarcliente.lower()=="silver":
			print "El Sr.(a): " + cliente +" posee tarjeta tipo: "+ tarcliente+ " por lo cual obtiene el 2%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			descuento = (compragen*0.02)
			totalcompra = compragen + iva - descuento
			print " "
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			print "__________________________"
			print " "
			efectivo = input("Cantidad de Pago en Efectivo: ")
			os.system('clear')
			print " "
			cambio = efectivo - compragen
			print "__________________________"
			print "__________________________"
			print " "
			print "NOMBRE: %s"%(cliente)
			print "NIT: %s"%(nit)
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
		# NINGUNA TARJETA Y PROCEDIMIENTO
		else:
			print "El Sr.(a): " + cliente +" no posee tarjeta de ningún tipo por lo que no obtiene el 5%. de DESCUENTO en todas sus compras"
			print " "
			print "El Subtotal de la factura sin iva es Q.%s"%(compragen)
			iva = (compragen*0.12)
			totalcompra = compragen + iva
			print "Debe: %s"%(totalcompra)
			print "__________________________"
			efectivo = input("Efectivo: ")
			cambio = efectivo - compragen
			print cliente
			print nit
			print "__________________________"
			print ("Precio       %.2f\t") % compragen
			print ("IVA          %.2f\t") % iva
			print ("Total        %.2f\t") % totalcompra
			print ("Efectivo     %.2f\t") % efectivo
			print "__________________________"
			print "Cambio:   %s"%(cambio)
			break
	print"Vuelva Pronto!"

#****************************************************************************************
#************************** Sub Menú para Opción Gerencia *******************************
#****************************************************************************************

def menugerencia():
	# CONTENIDO DEL MENU GERENCIA (OPCION 1 DEL MENU GENERAL)............................
	print "         ================================================================="
	print "         =======                                                   ======="
	print "         =======                                                   ======="
	print "         =======                                                   ======="
	print "         =======	                                           ======="
	print "         =======	                                           ======="
	print "         =======                 BIENVENIDO GERENTE                ======="
	print "         =======	         ==================                ======="
	print "         =======	                                           ======="
	print "         =======	                                           ======="
	print "         =======	                                           ======="
	print "         =======                                                   ======="
	print "         =======                                                   ======="
	print "         ================================================================="
	print " "
	time.sleep(2)
	print "A continuacion se le presenta las opciones que usted puede realizar en GERENCIA"
	print "                        QUE DESEA REALIZAR?????"
	print " "
	time.sleep(5)
	print " "
	print "######################################################"
	print "########   1. Ingreso de Productos          ##########"
	print "########   2. Regresar al Menu Principal:   ##########"
	print "######################################################"
	print " "
	print " "
	num_menur1 = raw_input("Por favor ingrese Numero de Opcion: ")
	print " "
	# VALIDACION DENTRO DEL MENU PARA REDIRECCIONAR.......................................
	if num_menur1 == "1":
		print "Usted a seleccionado la opcion de INGRESAR PRODUCTOS "
		os.system('cls')
		ingprod()
	elif num_menur1 =="2":
		os.system('cls')
		menuprincipal()
	else:
		print "Numero fuera de rango"
		os.system('cls')
		menugerencia()


#****************************************************************************************
#************************** Sub Sub Menú para Opción Ingreso de Productos ***************
#****************************************************************************************
def ingprod():
	# CONTENIDO DE INGRESO DE PRODUCTO (OPCION 1 DEL MENU GERENCIA)........................
	print "======================================================================"
	print u"A Seleccionado la Opción de Ingreso de Productos"
	print "======================================================================"
	value1=True
	# VALIDACION DE INGRESO DE PRODUCTO A LA TIENDA.......................................
	while value1==True:
		print " "
		print "      escriba SI o NO si "
		opcion =raw_input("Desea ingresar un producto: ")
		print " "
		try:
			if opcion.isalpha()==True:
				if opcion.lower()=="si":
					print " "
					nompro=raw_input("Ingrese Producto: ")
					prepro=input("Precio Unitario: ")
					unidades= input("Unidades a vender: ")
					total = prepro * unidades
					print "EL Total de el producto "+nompro
					print "           es de: "   + str (total)

					# ASIGNA VALOR A UNA CLAVE............................................
					prod_bodega[unidades]=[nompro,prepro]
				elif opcion.lower()=="no":
					value1=False
					os.system('cls')
				else:
					print u"Lo sentimos, opciones válidas 'si/no'; intentelo nuevamente"
			else:
				print u"Lo sentimos, no acepta números"
		except:
			value1=True
	# IMPRESION DE PRODUCTOS.............................................................
	print "Los Productos en Existencia son: "
	print " "
	for i in prod_bodega:
		time.sleep(1)
		print i,"Q.",prod_bodega[i]
		print " "
		time.sleep(4)

#****************************************************************************************
#************************** Menú Principal **********************************************
#****************************************************************************************
def menuprincipal():
	# CONTENIDO DE INGRESO DEL MENU PRINCIPAL............................................
	while menur == True:
		print " "
		print " "
		
		print " "
		time.sleep(1)
		print "======================================================================"
		print "======================================================================"
		print "==================================              " +       time.strftime("%I:%M  ") +  (time.strftime("%d/%m/%y"))     
		print "======================================================================"
		print " "
		print "                        B I E N V E N I D O     A:           "
		print "======================================================================"
		print "======================================================================"
		print "======================================================================"
		time.sleep(3)
		print "  (\o/)___________________________________________________________(\o/)"
		print "  (/o\)                                                           (/o\)"
		print "  (/o\)                 LIBRERIA EL PROGRAMADOR                   (/o\)"
		print "  (/o\)                                                           (/o\)"
		print "  (/o\)               ().....(),...'''''-._                       (/o\)"
		print "  (/o\)               `6_ 6  )   `-.  (     ).`-.__.`)            (/o\)"            
		print "  (/o\)               (_Y_.)'  ._   )  `._ `. ``-..-'             (/o\)"
		print "  (/o\)                  ..`--'_..-_/  /--'_. .                   (/o\) "
		print "  (/o\)               (il),-''  (li),'  ((!.-'                    (/o\)"
		print "  (/o\)___________________________________________________________(/o\)"
		print " "
		time.sleep(3)
		print "Por favor eliga una de las siguientes opciones :"
		print " "
		print "----------------."
		print ".  1. GERENCIA  ."
		print ".               ."
		print ".  2. CAJA      ."
		print "----------------'"
		print " "
		num_menur = raw_input("Ingrese Numero de Opcion que desee : ")
		print " "
		# ((((((((((((((((  VALIDACIONES de num_menur ))))))))))))))))
		if num_menur == "1":
			time.sleep(1)
			os.system('cls')
			contra = getpass.getpass("Por favor ingrese contrasenia: ")
			if contra =="123456789":
				print "COntraseña Correcta por favor espere:"
				time.sleep(2)
				os.system('cls')
				menugerencia()
			else: 
				print "Contraseña incorrecta"
				print "Sera regresado a el menu Principal"
				time.sleep(2)
				menuprincipal()
		elif num_menur =="2":
			time.sleep(2)
			os.system('cls')
			menucaja()
		else:
			os.system('cls')
			print "Numero fuera de Rango, Por Favor Vuelva a Intentarlo"
			print " "
menuprincipal()