#ejercicio de la clase 30/08/2021

from datetime import date 
class Empresa:
    def __init__(self,nom= "El mas barato",ruc="09999999" ,tel="09891663609",dir="Pedro Carbo"):
        self.nombre = nom 
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dir

    def mostrarEmpresa(self):
        print("Empresa: {:20} Ruc: {}".format(self.nombre, self.ruc))


from abc import ABC, abstractclassmethod, abstractmethod
class Cliente(ABC):
    def __init__(self,nom,ced,tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono= tel

    @abstractmethod
    def getCedula(self):
        return self.cedula

    def mostrarCliente(self):
        print(self.nombre, self.cedula, self.telefono)


class Articulo:
    secuencia= 0
    iva = 0.12
    def __init__(self,cod,des,pre,sto):
        self.codigo=cod
        self.descripcion=des
        self.precio=pre
        self.stock=sto
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)


class DetVenta:
    linea=0

    def __init__(self,articulo,cantidad):
        DetVenta.linea += 1
        self.lineaDetalle = DetVenta.linea
        self.articulo=articulo
        self.precio=articulo.precio
        self.cantidad=cantidad

class cabVenta:
    def __init__(self,fac,fecha,cliente,tot=0):
        self.factura=fac
        self.fecha=fecha
        self.cliente=cliente
        self.total=tot
        #detalle = DetVenta()
        self.detalleVen=[]

    def agregarDetalle(self,articulo,cantidad):
        detalle=DetVenta(articulo,cantidad)
        self.total += detalle.precio*detalle.cantidad
        self.detalleVen.append(detalle)

    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc: {}".format(empNombre, empRuc))
        print("Factura#:{:13}Fecha: {}".format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo      Precio  Cantidad  Subtotal")
        for det in self.detalleVen:
            print(" {:5} {:15} {} {:7}".format(det.linea,det.articulo, det.precio, det.cantidad, det.subtotal))
        print("Total Venta: {:26}".format(self.total))



class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel)
        self.__promocion=promocion

    @property
    #getter: obtener el valor del atributo privado
    def promocion(self):
        if self.__promocion == True:
            return "10% Descuento"
        else:
            return "No hay Promocion"

    # @contrato.setter
    # def contrato(self,value): #setter: asigna un valor al atributo privado
    #     self.__contrato = value


    def mostrarCliente(self):
        print("Cliente: {:13} Cedula: {}".format(self.nombre,self.promocion))


    def getCedula(self):
        return super().getCedula()

        
class ClienteCorporativo(Cliente):
     def __init__(self,contrato):
         self.__contrato=contrato

#     @property
#     # getter: obtener el valor del atributo privado
#     def contrato(self):
#         return self.__contrato

#     @contrato.setter
#     def contrato(self,value): #setter: asigna un valor al atributo privado
#         self.__contrato = value


#     def mostrarCliente(self):
#         print(self.nombre)


# cli= Cliente("Luis","099999394","098982432",True)

#emp= Empresa()
# emp.mostrarEmpresa()
# print(emp.nombre)

# cli1= ClientePersonal("Luis","099999394","098982432",True)
# print(cli1.getCedula())
# cli1.mostrarCliente()
# art1= Articulo(1,"Aceite",10,30)
# art1.mostrarArticulo()
# art2= Articulo(2,"colas",5,100)
# art2.mostrarArticulo()
# today=date.today()
# fecha=date(20,8,15)
# venta= cabVenta("F0001",date.today(),cli1)
# venta.agregarDetalle(art1,3)
# venta.agregarDetalle(art2,2)
# venta.mostrarVenta(empresa.nombre,empresa.ruc)

class InterfaceSistemaPAgo(ABC):
    @abstractmethod
    def pago(self):
        pass

    @abstractmethod
    def saldo(self):
        pass

class PagoTarjetaImplements(InterfaceSistemaPAgo):
    #este proceso hace el pago del calculo de intereses de la tarjeta
    def pago(self):
        return "Pago Tarjeta"

    def saldo(self):
        return "Saldo TarjetadeTrabajo"

class Vendedor():
    def __init__(self,nombre):
        self.nombre=nombre

    def moduloPago(self,pago):
        return contrato.Apago()

pagoTarjeta=PagoTarjetaImplements()
print(pagoTarjeta.pago())
pagoContrato = ImplementsPagoContrato()
#print(pagoContrato.pago())
ven1 = Vendedor("Luis")
print(ven1.moduloPago(Contrato.pago()))