'Some VBA code made to order a long accounting sheet

Sub acomodar_conceptos()
'comienza en a3 la lista, termina en a8088(8087 ultima llena). eso lo mido con columna b vacia(condicion del loop)
Range("a3").Select

Dim separador As String
separador = " // "

Do While ActiveCell.Offset(0, 0).Range("b1").Value <> ""
    Do While ActiveCell.Value <> "" And ActiveCell.Offset(0, 0).Range("a2").Value = ""
        'NO cambiar foco de offset aca
        'corta lo de a2 y lo une a lo de a1 separado por /
        ActiveCell.Offset(0, 0).Range("b1").Value = ActiveCell.Offset(0, 0).Range("b1").Value & separador & ActiveCell.Offset(0, 0).Range("b2").Value
        'elimina la fila de a2
        ActiveCell.Offset(0, 0).Range("a2").EntireRow.Delete
        'vuelve a activar el primer active cell para que se repita el loop de ser necesario(quiza esta de mas)
    Loop
ActiveCell.Offset(1, 0).Range("a1").Select 'bajo una y repito

Loop
'chequear si hay una ultima fecha mal(todas deberian quedar seguidas)
End Sub
