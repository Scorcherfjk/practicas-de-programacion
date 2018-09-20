def DINT(host, tags):
    from cpppo.server.enip.client import connector
    from cpppo.server.enip import client
    
    with connector( host=host ) as conn:
        for index,descr,op,reply,status,value in conn.pipeline(operations=client.parse_operations( tags ), depth=2 ):
            if value == True or value == False:
                yield value
            else:
                yield value[0]

def leerString(host,indice,etiqueta):
    from cpppo.server.enip.client import connector
    from cpppo.server.enip import client
    
    tags = ["RecetasPL[{}].{}.LEN".format(indice,etiqueta)]
    
    with connector( host=host ) as conn:
        for index,descr,op,reply,status,value in conn.pipeline(operations=client.parse_operations( tags ), depth=2):
            val = str(value[0])
            valor = ["RecetasPL[0].Medida.Data[0-"+val+"]"]
            with connector( host=host ) as conn:
                for index,descr,op,reply,status,value in conn.pipeline(operations=client.parse_operations( valor ), depth=2):
                    final = ''.join(chr(i) for i in value).strip("\x00")
                    return final